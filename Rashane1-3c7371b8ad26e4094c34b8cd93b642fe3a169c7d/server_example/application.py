from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" , name="dynamic" ,
                            num=randint(1, 100))
                            
@app.route("/goodbye")
def bye():
    return render_template("goodbye.html")