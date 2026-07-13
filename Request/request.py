from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Form</title>
</head>
<body>
    <form action="/login" method="POST">
    username: <input type="text" name="name" id="">
    <br>
    password: <input type="password" name="password" id="">
    <br>
    <input type="submit" value="login">
    
    
  </form>


</body>
</html>"""


@app.route("/login",methods=["GET","POST"])
def login():
    
    if request.method == "GET":
        username = request.form["name"]
        return "welcome " + username
    if request.method == "POST":
        username = request.form["name"]
        return "welcome " + username
    
if __name__ == "__main__":
    app.run(debug=True)