from flask import Flask, jsonify, render_template, request, redirect
from datetime import datetime


app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    form_response = jsonify(age = request.form['age'], name = request.form['name']);
    file_write_date = datetime.now();
    filename = f'{form_response[1]}{file_write_date}.json';
    submission = open(f'./{filename}', a+);
    return redirect('/confirmation')


@app.route('/confirmation')
def confirm_submit():
    return render_template('./templates/confirmation.html')

if __name__ == "__main__":
    app.run(debug=True)
