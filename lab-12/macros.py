from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    greeting = "home!"
    return render_template('macros_page.html',greeting=greeting)

@app.route('/about')
def about():
    greeting = "about!"
    return render_template('macros_page.html',greeting=greeting)

@app.route('/contact')
def contact():
    greeting = "contact!"
    return render_template('macros_page.html',greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
