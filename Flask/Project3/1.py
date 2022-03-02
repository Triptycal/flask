from flask import Flask,render_template

app=Flask(__name__)

@app.route("/info1")
def homepage1():
	return render_template("information.html",na="Mimi",addr="Tamworth",color="red")
@app.route("/info2")
def homepage2():
	return render_template("information.html",na="Ben",addr="Birmingham",color="green")
@app.route("/info3")
def homepage3():
	return render_template("information.html",na="Shafeeq",addr="Manchester",color="blue")
@app.route("/salaryslip/<name1>/<salary1>")
def salaryslip(name1,salary1):
    
	return render_template("salarySlip.html",name=name1,salary=int(salary1),color="white")   
	
app.run()
