import pymongo
import threading

def MongoDatabase():

    mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

    mongo_db = mongo_client['mydatabase']

    customer_collection = mongo_db['customers']

    customer_data = {
        "name": "Antony Stark",
        "age": 57
    }

    new_customer = customer_collection.insert_one(customer_data)

    print(new_customer.inserted_id)

threads = []

t = threading.Thread(target=MongoDatabase())
t.start()
threads.append(t)

for t in threads:
    t.join()