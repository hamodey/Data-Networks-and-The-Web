from flask import Flask, render_template
from flask import request
import feedparser

app = Flask(__name__)

<<<<<<< HEAD
RSS_FEEDS = { 'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
=======
RSS_FEEDS = { 'bbc': 'http://feeds.bbci.co.uk/sport/football/rss.xml',
>>>>>>> d26b24f1f403b657837d68de4d28ee48e746323b
              'aljazeera' : 'https://www.aljazeera.com/xml/rss/all.xml',
              'ap':\
              'http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5'}


@app.route("/")
def headlines():
    publication =''
    if request.args.get('publication'):
        publication = request.args.get('publication')
    if not publication or publication.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template('get_headlines.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
