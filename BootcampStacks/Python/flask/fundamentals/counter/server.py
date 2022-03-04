from datetime import datetime
from itertools import accumulate
from urllib import response

from flask import Flask, redirect, render_template, session, url_for, flash, session, sessions, request

app=Flask(__name__)
app.secret_key = 'cyCcv3VR9K6vYXuqz4dvbAhP_eFsKyJ2NKwq@--sZcCbDHkTN6'
app.session_cookie_name = 'accumulator'
accumulator = int

@app.route('/')
def visit_check():
    if accumulator == 0:
        collect_cookies = int
        template_accumulator = collect_cookies['accumulator']
        return redirect("/home/<int:template_accumulator>", template_accumulator=template_accumulator)
    else:
        session['accumulator'] = 0
        template_accumulator = session['accumulator'] = 0
        return redirect(url_for(index,template_accumulator=template_accumulator))
        
@app.route('/home/<int:template_accumulator>', methods=['GET', 'POST'])
def index(template_accumulator):
    template_accumulator = template_accumulator
    session['accumulator'] = request.form['accumulator']
    return render_template('index.html', template_accumulator=template_accumulator)

@app.route('/process', methods=['POST'])
def abacus(accumulator):
    accumulator = int(accumulator)
    session['accumulator']= request.form['accumulator']
    
    
    
@app.route('/reset')
def reset():
    session.clear()  # delete visits
    flash('Count Reset')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)