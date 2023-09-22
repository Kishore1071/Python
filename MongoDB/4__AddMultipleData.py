import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

customer_data = [
    {
        "name": "Bruce Banner",
        "age": 52
    },
    {
        "name": "Peter Parker",
        "age": 21
    }
]

new_customer = customer_collection.insert_many(customer_data)

print(new_customer.inserted_ids)