from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def home():
	return "Hi there"
@app.route('/sayhello/<name>')
def say_hello(name):
	return ("\t--->Hello {}".format(name))
	
app.run()