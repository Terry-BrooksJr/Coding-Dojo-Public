from flask import Flask,redirect,url_for,render_template,request,session
from datetime import datetime
app=Flask(__name__)
app.secret_key = 'cyCcv3VR9K6vYXuqz4dvbAhP_eFsKyJ2NKwq@--sZcCbDHkTN6'


@app.route('/',methods=['GET'])
def index():
    session['accumulator'] = request.form['accumulator']
    return render_template('index.html')

@app.route('/log_cookie')
def log_cookie():
    if 'visits' in session:
        # reading and updating session data
    session['visits'] = session.get('visits') + 1
    else:
    session['visits'] = 1  # setting session data
    return "Total visits: {}".format(session.get('visits'))

@app.route('/reset')
def reset():
    session.clear()  # delete visits
    return 'Visits deleted'

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
