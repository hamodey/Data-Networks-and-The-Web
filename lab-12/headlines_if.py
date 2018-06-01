from flask import Flask, render_template
import feedparser

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def headlines():
    feed = feedparser.parse(BBC_FEED)
    articles = feed['entries']
    return render_template('headlines.html',articles=articles)

@app.route("/<word>")
def headlines_word(word):
    word = word.lower()
    feed = feedparser.parse(BBC_FEED)
    articles = feed['entries']
    return render_template('headlines_if.html',articles=articles,word=word)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
