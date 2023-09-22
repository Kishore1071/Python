import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

customer_data = customer_collection.find().sort("name")

for x in customer_data:

    print(x)

# For desending order

customer_data = customer_collection.find().sort("name", -1)

for x in customer_data:

    print(x)