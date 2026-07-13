from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def login():
    return render_template("Login.html")

@app.route("/check", methods=["POST"])
def check():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "12345":
        session["user"] = username
        return redirect(url_for("Loginsf"))
    else:
        return "Invalid Login"

@app.route("/Login successful")
def Loginsf():
    return render_template("login successful.html")

if __name__ == "__main__":
    app.run(debug=True)