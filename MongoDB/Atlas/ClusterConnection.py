import pymongo

mongo_client = pymongo.MongoClient('mongodb+srv://Kishore:Kishore_Mongodb1071@cluster0.avdfxtj.mongodb.net/?retryWrites=true&w=majority')

mongo_db = mongo_client['mydatabase']

customer_collection = mongo_db['customers']

customer_data = {
    "name": "Antony Stark",
    "age": 57
}

new_customer = customer_collection.insert_one(customer_data)

print(new_customer.inserted_id)