from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def homepage():
	return render_template("home.html")
    
@app.route("/aboutus")
def message():
	return render_template("aboutus.html")
	
@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/nbs")
def boom():
	return "Welcome to Nationwide"
	
app.run()
