import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

# Create new collection if no existing collection have this name