from flask import Flask
from markupsafe import escape
from flask import render_template
import PCA9685
import time

app = Flask(__name__)
v = {}
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

@app.route("/")
def main():
    return render_template('/home.html', v=v)

@app.route("/api/motor/<motor>/<location>")
def move_base(motor, location):
    s = f"moving motor {escape(motor)} to {escape(location)}"
    if motor == "base":
        pwm.setServoPulse(10, 1250)
        time.sleep(0.02)
    print(s)
    return s