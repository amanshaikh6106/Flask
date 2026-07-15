from flask import Flask,render_template,request
import os
app=Flask(__name__)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER=os.path.join(BASE_DIR, "uploads")
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
os.makedirs(app.config["UPLOAD_FOLDER"],exist_ok=True)
@app.route("/")
def home():
    return render_template("select file.html")

@app.route("/upload",methods=["POST"])
def upload():
    file=request.files["file"]
    if file.filename=="":
        return "No file Selected"
    
    filename=file.filename
    file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
    return render_template("success.html",filename=filename)

if __name__=="__main__":
    app.run(debug=True)