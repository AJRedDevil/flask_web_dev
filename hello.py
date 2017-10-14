'''Initialization'''
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
'''
applicaton instance
Flask uses name argument to determine the root path of the application
so that it later can find resource files relative to the location of the
application.
'''
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    manager.run()
