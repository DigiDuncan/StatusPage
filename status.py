from flask import Flask, render_template, request, redirect, url_for
import arrow

app = Flask(__name__)

s = "LOADING"
d = "Digi forgot to update the page after refreshing the server..."
lu = arrow.now()
dis = "probably"


@app.route("/")
def home():
    return render_template("status.html", status=s, details=d, discord=dis, lastupdated=lu)


@app.route("/update")
def update_page():
    return render_template("update.html")


@app.route("/update", methods=["POST"])
def update():
    global s
    global d
    global lu
    status = request.form.get("status")
    details = request.form.get("details")
    if not status.endswith((".", "!", "?")):
        status += "."
    s = status
    d = details
    lu = arrow.now()
    return redirect(url_for("home"))
