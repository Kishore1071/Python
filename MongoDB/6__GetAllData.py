import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

# To limit the size of the dataset

data = customer_collection.find()

# data = customer_collection.find().limit(2)

# for x in data:

#     print(x)

# To get only specific fields in collections

for x in customer_collection.find({}, {"_id": 0,"name": 1, "age": 1}):

    print(x)

