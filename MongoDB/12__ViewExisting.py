import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

print(mongo_client.list_database_names())

mongo_db = mongo_client['mydatabase']

print(mongo_db.list_collection_names())
