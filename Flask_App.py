from flask import Flask,render_template,request
import sqlite3 as sql
import os

app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    from dbConnection.datamanipulation import sql_query
    row=sql_query("select * from employee_tb")
    return render_template('Home.html',details=row)

@app.route('/addEmployee')
def addEmployee():
    return render_template('addEmployee.html')


@app.route('/addAction',methods=['POST'])
def addAction():
    from dbConnection.datamanipulation import sql_edit_insert
    name = request.form['name']
    address = request.form['address']
    salary = request.form['salary']
    department = request.form['department']
    row=sql_edit_insert("insert into employee_tb VALUES(NULL,?,?,?,?)",(name,address,salary,department))
    return render_template('addEmployee.html')

@app.route('/deleteAction')
def deleteAction():
    from dbConnection.datamanipulation import sql_edit_insert,sql_query
    eid=request.args.get("id")
    row1=sql_edit_insert("delete from employee_tb where id=?",[eid])
    row=sql_query("select * from employee_tb")
    return render_template('Home.html',details=row)

if __name__ == '__main__':
     app.run(debug=True)

 
