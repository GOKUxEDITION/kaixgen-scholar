from pymongo import MongoClient
from config import MONGO_URI
from datetime import datetime

client = MongoClient(MONGO_URI)
db = client["kaixgen_scholar"]
users = db["users"]

def register_user(user_id, name):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({
            "user_id": user_id,
            "name": name,
            "board": None,
            "logs": []
        })

def set_board(user_id, board):
    users.update_one({"user_id": user_id}, {"$set": {"board": board}})

def get_user(user_id):
    return users.find_one({"user_id": user_id})

def add_log(user_id, subject, hours):
    users.update_one(
        {"user_id": user_id},
        {"$push": {
            "logs": {
                "subject": subject,
                "hours": hours,
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        }}
    )
