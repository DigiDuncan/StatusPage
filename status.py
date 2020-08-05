from flask import Flask, render_template
import arrow

app = Flask(__name__)

s = "dead"
d = "(not really)"
dis = "online"
lu = arrow.now()


@app.route("/")
def home():
    return render_template("status.html", status=s, details=d, discord=dis, lastupdated=lu)
