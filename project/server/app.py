from flask import Flask, render_template

#app = Flask(__name__, template_folder='../templates')
app = Flask(__name__, template_folder='../client', static_url_path='', static_folder='../client')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)