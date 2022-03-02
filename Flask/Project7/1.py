from flask import Flask,render_template, request, session, redirect
app=Flask(__name__)
app.secret_key = 'nationwide'

@app.route("/")
def page1():
    
	return render_template("page1.html")   

@app.route("/page2/<T>")
def page2(T):
    session["timestable"]=int(T)
	return render_template("page2.html")   

@app.route("/page3/<R>")
def page3(R):
    if not session.get('timestable'):
        return redirect("/")
    else:
        return render_template("timestable.html",Range=int(R)) 
            
@app.route("/clear")
def clear():
    session.clear()
	return redirect("/")
    
app.run(debug=True)
