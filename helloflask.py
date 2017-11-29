from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(8, GPIO.OUT, initial=0)
GPIO.setup(7, GPIO.OUT, initial=0)

app = Flask(__name__)

id_to_led = {'1':8, '2':7}

@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y %H:%M")
	templateData = {
		'title' : 'Hello',
		'time' : timeString
		}
	return render_template('index.html', **templateData)

@app.route("/on/<led>", methods=['POST'])
def on(led):
	#print(led)
	#print(id_to_led[led])
	GPIO.output(id_to_led[led], GPIO.HIGH)
	return "on"

@app.route("/off/<led>", methods=['POST'])
def off(led):
	#print(led)
	#print(id_to_led[led])
	GPIO.output(id_to_led[led], GPIO.LOW)
	return "off"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)

