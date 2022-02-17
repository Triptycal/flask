from flask import Flask

app=Flask(__name__)

@app.route("/aboutus")
def message():
	return "Hello friends"

@app.route("/nbs")
def boom():
	return "Welcome to Nationwide"
	
app.run()
