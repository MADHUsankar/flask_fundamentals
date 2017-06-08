from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/<username>')
def greeting(username):
   return render_template("index.html",name=username)

@app.route('/ninjas')
def ninjasdetails():
   return render_template("ninjas.html")


@app.route('/dojos/new')
def newform():
   return render_template("dojo.html")

app.run(debug=True)