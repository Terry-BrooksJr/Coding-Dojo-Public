from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.secret_key = 'zwz7dvq6ycz9PNJ-hqr'

@app.route('/',methods=['GET','POST'])
def home():
    session
    return render_template('index.html')

@app.route('/log_visit')
def log_cookie():
    
    return render_template('expression')
@app.route('/reset')
def reset():
    session.clear()
    return render_template('expression')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)