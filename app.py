from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
v = {}
@app.route("/")
def main():
    return render_template('/home.html', v=v)

@app.route("/api/motor/<motor>/<location>")
def move_base(motor, location):
    s = f"moving motor {escape(motor)} to {escape(location)}"
    print(s)
    return s