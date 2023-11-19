import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

"""

NOTE:

Database will never create untill we create a collection and add data to that collection

"""
