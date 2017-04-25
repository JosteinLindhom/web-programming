"""
Exercise #1: Remembering user details
"""

from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import datetime

app = Flask(__name__)
app.debug = True  # only for development!
app.secret_key = "jW6nx1jaFeWMgMZoDJXNIV3FFmIEG0sUaLPU4ezsp7u04ztDLtjIiqk0Zl9sRMYtsSXyAEsfbTA1DYf4ZWETjA=="


@app.route("/")
def index():
    name = request.cookies.get("name", None)
    email = request.cookies.get("email", None)
    return render_template("page.html", name=name, email=email)


@app.route("/save", methods=["POST"])
def save():
    name = None
    email = None
    if "name" in request.form:
        name = request.form["name"]
    else:
        flash("Name is missing", "error")
    if "email" in request.form:
        email = request.form["email"]
    else:
        flash("Email is missing", "error")

    response = make_response(redirect(url_for("index")))
    if name and email:
        expiry = datetime.datetime.now() + datetime.timedelta(days=60)
        response.set_cookie("name", name, expires=expiry)
        response.set_cookie("email", email, expires=expiry)
        flash("User details remembered", "success")

    return response


@app.route("/forget")
def forget():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("name", "", expires=0)
    response.set_cookie("email", "", expires=0)
    flash("User details forgotten", "success")
    return response


if __name__ == "__main__":
    app.run("0.0.0.0")
