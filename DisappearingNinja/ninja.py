from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def noninja():
  return render_template("noNinja.html")

@app.route('/ninja')
def ninjafour():
  return render_template("ninjaFour.html")
 
@app.route('/ninja/<color>')
def ninjacolor(color):
  return render_template("ninjaColor.html",color=color)
 

app.run(debug=True) 