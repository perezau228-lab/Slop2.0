"""
test_server.py
--------------
A deliberately insecure local test target -- a login form that
accepts plain HTTP POST data. This exists ONLY so you have something
safe and legal to point your sniffer at.

Run this, then run your sniffer with a filter for this port, then
submit the form (or use curl) and watch your sniffer catch it.

DO NOT deploy this anywhere real. It's intentionally insecure.
"""

from flask import Flask, request

app = Flask(__name__)

LOGIN_FORM = """
<form method="POST" action="/login">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit">
</form>
"""


@app.route("/", methods=["GET"])
def home():
    return LOGIN_FORM


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Received login attempt for user: {username}"


if __name__ == "__main__":
    # Deliberately plain HTTP (no ssl_context) -- that's the point.
    app.run(host="127.0.0.1", port=5000, debug=False)
