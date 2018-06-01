from pymongo import MongoClient

def db_connect():
	
	try:
		client = MongoClient('mongodb://localhost:27017/')
	except:
		print("Error: failed to create mongo client")
		raise
	
	else:
		
		db = client.catflucks
		return db

