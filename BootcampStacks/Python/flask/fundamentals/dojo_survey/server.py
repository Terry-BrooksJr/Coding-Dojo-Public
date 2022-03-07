from flask import Flask,redirect,url_for,render_template,request,session,jsonify
import json 

app=Flask(__name__)
app.secret_key = 'cyCcv3VR9K6vYXuqz4dvbAhP_eFsKyJ2NKwq@--sZcCbDHkTN6'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST','GET'])
def process():
    submission = {}
    submissions[request.form['name']] = {'name':}
    ninja_name = [request.form['name']],
    dojo_location= [request.form['location']],
    fav_prog_lang = [request.form['language']]
    submission =[ninja_name,dojo_location,fav_prog_lang]
    with open('submissions','w') as submission_file:
         json.dump(submission, submission_file) 
    return redirect(url_for('confirmation'),308)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation_page.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
