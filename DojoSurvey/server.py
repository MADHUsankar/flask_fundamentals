from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

 

@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   print request.form 

   name = request.form['name']
   location = request.form['location']
   favlang = request.form['favlang']
   return render_template('result.html',name=name,location=location,favlang=favlang)
   return redirect('/')
app.run(debug=True) 