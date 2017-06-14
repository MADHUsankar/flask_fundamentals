from flask import Flask, render_template, request, redirect,flash,session
app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
  return render_template("FORM.html")

 

@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   print request.form 

   firstname = request.form['firstname']
   lastname = request.form['lastname']
   password = request.form['password']
   pw_confirm = request.form['pw_confirm']


   if len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(pw_confirm) < 1:
      if len(firstname) < 1:
        flash("Please enter First name")
      if len(lastname) < 1:
        flash("Please enter Last name")
      if len(password) < 1:
        flash("Please enter Password")
      if len(pw_confirm) < 1:
        flash("Please reenter Password")
      return redirect('/')
    
   if password!=pw_confirm:
        flash("Password doesnot match")
        return redirect('/')

  

   return render_template("result.html", name=firstname + " " + lastname)
   return redirect('/')
app.run(debug=True) 