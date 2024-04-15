from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "website is alive"

#app.run()