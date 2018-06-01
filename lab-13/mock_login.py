from flask import Flask, render_template
from flask import request, flash
import string

app = Flask(__name__)

USERNAME, PASSWORD = 'alan', '4l4n'
<<<<<<< HEAD
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
=======
app.secret_key = 'ihatednw'
>>>>>>> d26b24f1f403b657837d68de4d28ee48e746323b

def sanitise_string(userinput):
    return ''.join(e for e in userinput if e.isalnum())
    # https://docs.python.org/3.5/library/stdtypes.html

@app.route("/", methods = ['GET','POST'])
def show_user():
    username, password ='',''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        username = sanitise_string(username)
        password = sanitise_string(password)
        
        if username == USERNAME and password == PASSWORD:
<<<<<<< HEAD
           flash('login successful!') 
=======
           flash('login successful!')
        else:
            flash('FAILED Y U TRYNA H4CK!?') 
>>>>>>> d26b24f1f403b657837d68de4d28ee48e746323b
    list = [username, password]
    return render_template('mock_login.html', list=list)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
