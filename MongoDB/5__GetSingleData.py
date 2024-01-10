import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

# To get the first data from the collection

data = customer_collection.find_one()

print(data)

