import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

delete_query = {
    "name": "Peter Parker"
}

# deleted_data = customer_collection.delete_one(delete_query)

# To delete all data

customer_collection.delete_many({})

# print(deleted_data.deleted_count, "Rows deleted")