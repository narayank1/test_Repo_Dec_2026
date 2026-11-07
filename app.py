# this is the test file to test the code and ggithub actions.
# checking the linting flask. test the push tested and corrected
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/health")
def health():
    return "Server is up and running"
