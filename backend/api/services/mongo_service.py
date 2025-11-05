from pymongo import MongoClient
import os

mongo_client = MongoClient(os.getenv("MONGO_URL", "mongodb://mongo:27017"))
db = mongo_client["salesboost"]

def get_product_info(product_id):
    return db.products.find_one({"id": product_id}, {"_id": 0})
