from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderHome():
  return render_template("home.html")


app.run(port=5000, debug=True)