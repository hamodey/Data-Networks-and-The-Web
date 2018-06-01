from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1>  Hello, World!  </h1></center>'

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M:%S'):
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route('/time')
def show_time():
    return render_template('show_time_with_filter.html', time=datetime.datetime.now())
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
