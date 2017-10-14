'''Initialization'''
from flask import Flask
'''
applicaton instance
Flask uses name argument to determine the root path of the application
so that it later can find resource files relative to the location of the
application.
'''
app = Flask(__name__)

@app.route('/')
def index():
    return '<div>Hello world!<div>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % (name)

if __name__ == "__main__":
    app.run(debug=True)
