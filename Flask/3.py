from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
	return """
		<html>
		<center><h1>Welcome to my Homepage</h1></center>
		We are the only building society in the united kingdom
		<br>
		<br>
		<a>Who we are</a> <br>
		<a href="http://localhost:5000/services"> Our Services </a><br>
		</html>
		"""
	
@app.route("/aboutus")
def message():
	return "<b>Hello</b> <u>friends</u>"
	
@app.route("/services")
def services():
	return """
		<html>
		<center><h2>We provide the following services</h2></center>
		<br>
		<a href="http://localhost:5000"> Home </a><br>
		<br>
		<ul>
			<li>Open account</li>
			<li>Deposit Money</li>
			<li>Withdraw Money</li>
		</ul>
		</html>
		"""

@app.route("/nbs")
def boom():
	return "Welcome to Nationwide"
	
app.run()
