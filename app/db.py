from pymongo import MongoClient
from datetime import datetime

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["voice_gender_db"]
collection = db["predictions"]

def log_prediction(file_name, gender):
    """
    Logs the prediction details to MongoDB.

    Parameters:
    - file_name (str): Name of the audio file.
    - gender (str): Predicted gender.
    """
    now = datetime.now()
    record = {
        "file_name": file_name,
        "date": now.strftime("%m/%d/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "gender": gender
    }
    collection.insert_one(record)
