from datetime import datetime
from itertools import accumulate
from urllib import response

from flask import Flask, redirect, render_template, session, url_for, flash, session, sessions, request

app=Flask(__name__)
app.secret_key = 'cyCcv3VR9K6vYXuqz4dvbAhP_eFsKyJ2NKwq@--sZcCbDHkTN6'


@app.route('/')
def  index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def abacus(accumulator):
    accumulator = int(accumulator)
    session['accumulator']= request.form['accumulator']
    return redirect(url_for(index))

@app.route('/reset')
def reset():
    session.clear()  # delete visits
    flash('Count Reset', "info")
    return redirect(url_for(index))

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)