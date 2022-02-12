from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/<int:side1>/<int:side2>')
def home(side1, side2):
    return render_template('index.html',side1=side1,side2=side2)

if __name__ == '__main__':


#DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)