from flask import Flask, render_template
app=Flask(__name__)


student = {
    "name": "Aman",
    "age": 20,
    "city": "New York",
    "subjects": ["Python", "Flask", "HTML", "CSS", "JavaScript"]
}

@app.route('/')
def home():
	return render_template("index.html", student=student)
	

@app.route('/about')
def about():
	return render_template("about.html", student=student)

@app.route('/contact')
def contact():
	return render_template("contact.html", student=student)

if __name__=="__main__":
	app.run(debug=True)