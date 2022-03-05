from flask import Flask,redirect,url_for,render_template,request,session,jsonify
import json 

app=Flask(__name__)
app.secret_key = 'cyCcv3VR9K6vYXuqz4dvbAhP_eFsKyJ2NKwq@--sZcCbDHkTN6'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST','GET'])
def process():
    print(request.form)
    # submissions[request.form['name']] = {'name':request.form['name']}
    # submissions[request.form['location']] = {'dojo_location': request.form['location']},
    # # submissions[request.form['name']] = {'fav_prog_lang': request.form['language']}
    # with open('submissions','w') as submission_file:
    #     json.dump(submissions, submission_file)
    return redirect(url_for('confirmation'),308)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation_page.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
