from flask import Flask,render_template

app=Flask(__name__)

@app.route("/homePage")
def homePage():
    
	return render_template("homePage.html")   

@app.route("/timesTable/<num>")    
def timesTable(num):
    
	return render_template("timesTable.html",T=int(num))  
	
app.run()
