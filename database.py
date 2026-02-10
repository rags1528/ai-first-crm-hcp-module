from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)

db = client["hcp"]   # your database name
interaction_collection = db["user_data"]   # your collection
