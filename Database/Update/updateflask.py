from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/form", methods=["GET"])
def update_form():
    return render_template("form.html")

@app.route("/update", methods=["POST"])
def update():
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
    sql = """UPDATE stud SET name = %s, age = %s, course = %s WHERE student_id = %s"""
    values = (name, age, course, student_id)
    cursor.execute(sql, values)
    con.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    con.close()

    if rows_affected == 0:
        return "No student found with that ID."
    return "Updated Successfully"

if __name__ == "__main__":
    app.run(debug=True)