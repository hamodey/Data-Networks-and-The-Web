from flask import Flask, render_template
from flask import request, flash
import string
from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import validators

class LoginForm(Form):
    username = StringField('username', validators = [validators.DataRequired()])
    password = PasswordField('password', validators =[validators.DataRequired(), validators.length(min=8)])
    password2 = PasswordField('password2', validators=[validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])


app = Flask(__name__)

USERNAME, PASSWORD = 'alan', '4l4n4l4n'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def sanitise_string(userinput):
    return ''.join(e for e in userinput if e.isalnum())
    # https://docs.python.org/3.5/library/stdtypes.html

@app.route('/', methods = ['GET', 'POST'])
def login():
    username, password ='',''
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        if username == USERNAME and password == PASSWORD:
<<<<<<< HEAD
           flash('login successful!') 
=======
           flash('login successful!')
        else:
            flash('FAILED STOP TRYNA HACK') 
>>>>>>> d26b24f1f403b657837d68de4d28ee48e746323b
    list = [username, password]
    return render_template('mock_login_wtforms.html', form=form, list=list)




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
