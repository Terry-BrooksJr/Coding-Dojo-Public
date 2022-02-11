from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<num_of_boxes:num>',num_of_boxes=3)
def home(num_of_boxes, ):
    boxes = " "
    
    for i in range(0, num_of_boxes):
        boxes += f'<div class = "blue-box" > </div >'
        return boxes