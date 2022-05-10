from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello, World!</p>"

@app.route("/api/motor/<motor>/<location>")
def move_base(motor, location):
    s = f"moving motor {escape(motor)} to {escape(location)}"
    print(s)
    return s