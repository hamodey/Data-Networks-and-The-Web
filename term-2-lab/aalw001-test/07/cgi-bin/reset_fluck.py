
from utils import db_connect

from bson.objectid import ObjectId

db = db_connect()

num_flucks = 0

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hello Caflucks</title>
</head>
<body>
<h1>Welcome to Catflucks</h1>""")


result = db.images.aggregate(
	[{ '$sample': { 'size': 1 } }]
)

if result:
	# 
	for img in result:
		img_src = img['url']
		img_alt = img['alt']
		img_id = img['_id']

	num_flucks = db.flucks.find( {"image_id": ObjectId(img_id), "is_flucked":1} ).count()

	print("""<p>You are viewing a random image of a cat.</p>
	<img src="{}" alt="{}" width=500>
	<p>This poor cat has been flucked {} times already.</p>
	<a href="/cgi-bin/serve_cat.py" title="serve cat">Serve new cat</a>
	""".format( img_src, img_alt, str(num_flucks) ))
else:
	print("<p>Oops. Something went wrong!</p>")

# output some footer html
print("</body></html>")


