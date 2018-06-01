from flask import Flask, render_template
from flask import redirect, url_for
from vs_url_for import vs_url_for

app = Flask(__name__)

@app.route('/')
def home():
    greeting = "this route is root"
    return render_template('macros_page.html',greeting=greeting)

@app.route('/login')
def login():
    # doing some login stuff
    return redirect(vs_url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
