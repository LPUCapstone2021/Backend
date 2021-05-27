import os
import pymongo
# from bson.objectid import ObjectId
import json
from dotenv import load_dotenv
from bson import json_util

load_dotenv() 

client = pymongo.MongoClient(f'mongodb+srv://root:{os.getenv("MONGO_PASSWORD")}@cluster0.3jfuq.mongodb.net/Database?retryWrites=true&w=majority')

db = client['Database']
collection = db['cars']

def car_details(ids):
    cars = collection.find({'id': {'$in': ids}})
    return json.loads(json_util.dumps(cars))
