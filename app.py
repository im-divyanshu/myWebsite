from flask import render_template,Flask,request
import requests

app=Flask(__name__)

@app.route("/")
def HomePage():
    return render_template("index.html")
@app.route("/writting")
def writting():
    return render_template("my_hobbies_writting.html")
@app.route("/more")
def more_section():
    return render_template("more.html")
@app.route("/contact")
def load_contact_page():
    return render_template("contact.html")
@app.route("/projects")
def load_projects_page():
    return render_template("projects.html")
