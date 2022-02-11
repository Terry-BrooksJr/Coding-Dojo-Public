from flask import Flask
from names import names
from random import randint

app = Flask(__name__)

@app.route('/')
def hello_world():
    for name in names:
        random_name = names[randint(0,50)]
    print(f'Welcome to the World Wide Web, I am your Web Server, {random_name} Great to meet you, What am I serving up')
@app.route('/dojo')
def dojo():
    print('Dojo')

@app.route('/say/<name>')
def personal_greeting(name):
    print(f'g\'day mate! I hear your name is {name} ')

@app.route('/repeat/<num_of_iterations>/<echo_word>')
def parroting(num_of_iterations,echo_word):
    print(echo_word * int(num_of_iterations))