import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

selecter_query = {"name": "Bruce Banner"}
new_data = {"$set": {"age": 30}}

# update_data = customer_collection.update_one(selecter_query, new_data)

# To Update many data

update_data = customer_collection.update_many(selecter_query, new_data)