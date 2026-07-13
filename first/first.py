from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Home Page'

@app.route('/about')
def about():
    return 'This is the About Page'

@app.route('/contact')
def contact():
    return 'This is the Contact Page'

@app.route('/<name>')
def hello(name):
    return "i am good " + name

if __name__ == '__main__':
    app.run(debug=True)