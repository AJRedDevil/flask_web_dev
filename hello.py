'''Initialization'''
from flask import Flask, request, make_response, redirect
'''
applicaton instance
Flask uses name argument to determine the root path of the application
so that it later can find resource files relative to the location of the
application.
'''
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.example.com')
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
    return '<h1>Bad Request</h1>', 400
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
    return '<div>Hello world!<div>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % (name)

if __name__ == "__main__":
    app.run(debug=True)
