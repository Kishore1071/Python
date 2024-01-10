import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['Marvel']

customer_collection = mongo_db['customers']

data = customer_collection.find({id: '659ea30a87d2be4d78191b89'})

for x in data:

    print(x)

