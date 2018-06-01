from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '<center><h1>  hello, %s  </h1></center>' % username

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
