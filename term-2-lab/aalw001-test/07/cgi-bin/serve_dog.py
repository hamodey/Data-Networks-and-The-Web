#!/usr/bin/env python3

from utils import db_connect

# make bson ObjectId class available for referencing 
# bson objects inside a mongo query string
from bson.objectid import ObjectId 

# connect to database
db = db_connect()

# output some header html
print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hello Dogflucks</title>
</head>
<body>
<h1>Welcome to Dogflucks</h1>""")


# get one random document from images collection
result = db.people.aggregate(
	[{ '$sample': { 'size': 1 } }]
)

# if a result came back
if result:
	# iterate through objects in the cursor (should only be 1)
	for img in result:
		# pull out the img url and alt text
		img_src = img['url']
		img_alt = img['alt']
		img_id = img['_id']

	# find and count flucks with matching img_id and where is_flucked is 1
	print("""<p>You are viewing a random image of a cat.</p>

       	<img src="{}" alt="{}" width=500>
	<a href="/cgi-bin/serve_cat.py" title="serve cat">Serve new cat</a>
	<a href="/cgi-bin/serve_dog.py" title="serve dog">Serve new Dog</a>
	""".format( img_src, img_alt))

else:
	print("<p>Oops. Something went wrong!</p>")

# output some footer html
print("</body></html>")

