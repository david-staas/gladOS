from flask import Flask
from markupsafe import escape
from flask import render_template
from PCA9685 import PCA9685
import time
import RPi.GPIO as GPIO

app = Flask(__name__)
v = {}
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # LED is on GPIO pin 17

head_last = 1500;
@app.route("/")
def main():
    return render_template('/home.html', v=v)

@app.route("/api/motor/<motor>/<int:location>")
def move_base(motor, location):
    global head_last
    s = f"moving motor {escape(motor)} to {escape(location)}"
    if motor == "base":
        pwm.setServoPulse(0, location)
        time.sleep(0.02)
    elif motor == "shoulder":
        pwm.setServoPulse(2, location)
        time.sleep(0.04)
    elif motor == "elbow":
        pwm.setServoPulse(4, location)
        time.sleep(0.04)
    elif motor == "head":
        pwm.setServoPulse(6, location)
        time.sleep(0.005)
        # if head_last > location:
        #     start = location
        #     end = head_last
        # else:
        #     start = head_last
        #     end = location
        # for i in range(start, end):
        #     pwm.setServoPulse(6, i)
        #     time.sleep(0.005)
        #     head_last = i
    print(s)
    return s

@app.route("/api/led/<int:led_pin>/<value>")
def control_led(led_pin, value):
    if value == "on":
        GPIO.output(led_pin, GPIO.HIGH)
    elif value == "off":
        GPIO.output(led_pin, GPIO.LOW)
    
    