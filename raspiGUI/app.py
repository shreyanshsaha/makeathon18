from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderHome():
  render_template("home.html")