from flask import Flask,render_template, request, redirect
import mysql.connector
app=Flask(__name__)

bd=mysql.connector.connect( host="localhost",
                            user="root",
                            password="root",
                            database="flask"
                            )
mycursor=bd.cursor()

@app.route("/")
def homePage():
    mycursor.execute("select * from personal")
    records=mycursor.fetchall();
    
    return render_template("HomePage.html",data=records)   

@app.route("/departments/<dept>")    
def departmentlist(dept):
    
    mycursor.execute("select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();
    
    return render_template("HomePage.html",data=records)   

@app.route("/details/<empno>")     
def details(empno):
    
    mycursor.execute("select * from personal where empno='"+empno+"'")
    personalrecord=mycursor.fetchall();
    mycursor.execute("select * from accounts where empno='"+empno+"'")
    salaryrecords=mycursor.fetchall();
    return render_template("details.html",personal=personalrecord,accounts=salaryrecords)   
    
@app.route("/newrecord")     
def newrecord():

    return render_template("inputform.html")  
    
@app.route("/newrecordsalary")     
def newrecord2():

    return render_template("payslipinputform.html")  

@app.route("/saverecord",methods=["POST"])     
def saverecord():
    
    name=request.form["na"]
    dept=request.form["dept"]
    sql1="insert into personal (name,department) values('{0}','{1}')".format(name,dept)
    mycursor.execute(sql1)
    bd.commit()
    
    return redirect("/")   


@app.route("/saverecord2",methods=["POST"])     
def saverecord2():
    empno=request.form["empno"]
    amount=request.form["salary"]
    sql1="insert into accounts (empno,salaryDate,amount) values({0},now(),{1})".format(empno,amount)
    mycursor.execute(sql1)
    bd.commit()
    
    return redirect("/")   
    
@app.route("/employeelist",methods=["POST"])     
def employeelist():
    dept=request.form["dept"]
    if dept=="all":
        mycursor.execute("select * from personal")
    else:
        mycursor.execute("select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();
    return render_template("HomePage.html",data=records)
    
app.run(debug=True)
