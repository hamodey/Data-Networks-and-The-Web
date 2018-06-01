from flask import Flask
from datetime import datetime
app = Flask(__name__)




@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/time')
def real_time():
        return str(datetime.now())

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0' ,port=8000)
