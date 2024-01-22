import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

# data = customer_collection.find({'name': "Bruce Banner"})

# for x in data:

#     print(x)

# for x in customer_collection.find({}, {}):

#     print(x)

# for x in customer_collection.find({}, {"_id": 0,"name": 1}):

#     print(x)

filter_query = {"age": {"$gt": 20, "$lt": 50}}

for x in customer_collection.find(filter_query, {"_id": 0,"name": 1}):

    print(x)

