from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return render_template("success.html")
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        gender = request.form.get("gender")
        college = request.form.get("college")
        event = request.form.get("event")
        mode = request.form.get("mode")
        comments = request.form.get("comments")

        print(name, email, mobile, gender, college, event, mode, comments)

        return render_template("success.html")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True,port=5001)
