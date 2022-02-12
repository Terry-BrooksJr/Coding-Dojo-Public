from flask import Flask,redirect,url_for,render_template,request
from random import random



@app.route('/')
def render_table():
    users= [
{'first_name': 'Michael', 'last_name': 'Choi'},
{'first_name': 'John', 'last_name': 'Supsupin'},
{'first_name': 'Mark', 'last_name': 'Guillen'},
{'first_name': 'KB', 'last_name': 'Tonel'}
]

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)