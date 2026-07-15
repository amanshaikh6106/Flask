from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("form1.html")

@app.route("/save", methods=["POST"])
def save():
    student_id = request.form.get("student_id")
    name = request.form.get("name")
    age = request.form.get("age")
    course = request.form.get("course")
    con = mysql.connector.connect(
        host="localhost",
        user="Aman",
        password="Aman@6106",
        database="my_database"

    )
    cursor = con.cursor()
    sql = """INSERT INTO stud(student_id, name, age, course)values(%s, %s, %s, %s)"""
    values = (student_id, name, age, course)
    cursor.execute(sql, values)
    con.commit()
    cursor.close()
    con.close()
    return "Inserted Successfully"


if __name__ == "__main__":
    app.run(debug=True)