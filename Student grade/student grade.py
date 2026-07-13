from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/grade", methods=["POST"])
def grade():

    name = request.form["name"]
    english = int(request.form["english"])
    maths = int(request.form["maths"])
    science = int(request.form["science"])

    total = english + maths + science
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return render_template(
        "result.html",
        name=name,
        total=total,
        percentage=percentage,
        grade=grade
    )

if __name__ == "__main__":
    app.run(debug=True)