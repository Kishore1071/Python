import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

customer_collection.drop()