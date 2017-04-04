"""
Exercise #1: Checking username
"""
import re
from flask import Flask, request

app = Flask(__name__)


@app.route("/check_username")
def check_username():
    # this list contains the usernames taken
    USERNAMES = ["johnsmith", "maryjane", "johndoe", "smith"]

    username = request.args.get("username", None)
    print(username)
    if username:
        if len(username) < 3:
            print("too short")
            return "Username is too short."
        elif not username.isalnum():
            print("is not alnum")
            return "Username may only contain letters or digits."
        elif username in USERNAMES:
            print("taken")
            return "Name is already taken."
    print("ok")
    return ""


@app.route("/")
def index():
    return app.send_static_file("exercise1.html")


if __name__ == "__main__":
    app.run()
