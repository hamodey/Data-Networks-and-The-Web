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
    submit = SubmitField('submit', [validators.DataRequired()])


app = Flask(__name__)

USERNAME, PASSWORD = 'ahmed', 'password'

app.secret_key = '1234567890'

def sanitise_string(userinput):
    return ''.join(e for e in userinput if e.isalnum())

@app.route('/login', methods = ['GET', 'POST'])
def login():
    username, password ='',''
    form = LoginForm()
    if form.validate_on_submit():
        print('printing')
        password = form.password.data
        username = form.username.data
        print(password, "this is passwrod")
        if username == USERNAME and password == PASSWORD:
           flash('login successful!')
        else:
            flash('FAIL') 
    list = [username, password]
    return render_template('loginwtf.html', form=form, list=list)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

