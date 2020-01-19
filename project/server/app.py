from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

#app = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../templates')
app = Flask(__name__, template_folder='../client', static_url_path='', static_folder='../client')

app.config['SECRET_KEY'] = 'a0e3969c13f75e6e6b51d3b154b21839'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)