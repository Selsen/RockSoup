# This program will help the user determine, which type of rock the person has found. 
# The user types properties of the rock, like color, porosity etc. The program combines the user input with properties of know rocks and suggests these
# I.e. User types 'Pink', Computer outputs 'It could be/contain Rosenkvarts'. 'It could be/contain feldspar coloured with iron and mixed with
# something else that makes it pink'

# Make a seperat window for the interaction
# Import a framework so I can use GUI
from flask import Flask, render_template, request
app = Flask(__name__)


# Calls code that sits on the root of the local host URL 
@app.route("/")
def root(): 
	return render_template('roothtml.html')


# Calls code concerning input field
@app.route('/rock', methods= ['POST', 'GET'])
def rock(): 
   if request.method == 'POST':
      rock = request.form
      return render_template('colors.html', rock = rock)
	



# ---------------------------------------------------
# Run everything written above these lines ----------
# ---------------------------------------------------
if __name__ == "__main__":
	app.run()