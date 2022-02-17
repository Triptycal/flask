from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
	return "<h1> welcome to my homepage</h1>"
	
@app.route("/aboutus")
def message():
	return "<b>Hello</b> <u>friends</u>"

@app.route("/nbs")
def boom():
	return "Welcome to Nationwide"
	
app.run()
