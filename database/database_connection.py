from pymongo import MongoClient
from pymongo.server_api import ServerApi


def load_mongo():
    uri = "mongodb://localhost:27017"


    client = MongoClient(uri, server_api=ServerApi('1'))
    return client
# Creates connection with Atlas.

# database = client["student_db"]
#
#
# student_collection = database["students"]