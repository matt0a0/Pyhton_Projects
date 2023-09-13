from pymongo import MongoClient

def get_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['user_cards_registration']
    return db
