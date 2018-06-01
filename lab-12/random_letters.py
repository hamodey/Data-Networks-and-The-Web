from flask import Flask
import random
import string

app = Flask(__name__)

words = ['a','random', 'word','list']

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word')
def word():
    word =  ''.join([random.choice(string.ascii_letters) for n in range(32)])
    print(word)
    return word

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
