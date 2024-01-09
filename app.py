from flask import render_template,Flask,request

app=Flask(__name__)

@app.route("/")
def HomePage():
    return render_template("index.html")
@app.route("/writting")
def writting():
    return render_template("my_hobbies_writting.html")