from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    age = request.form["age"]
    gender = request.form["gender"]
    password = request.form["password"]

    if name != "admin" or password != "admin@123":
        return render_template(
            "register.html",
            error="Invalid name or password."
        )

    return render_template(
        "success.html",
        name=name,
        email=email,
        phone=phone,
        age=age,
        gender=gender
    )

if __name__ == "__main__":
    app.run(debug=True)