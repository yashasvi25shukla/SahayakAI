# ==========================================
# SAHAYAKAI - MONGODB DATABASE CONNECTION
# ==========================================

import os

from dotenv import load_dotenv
from pymongo import MongoClient


# Load .env
load_dotenv()


# ==========================================
# MONGODB SETTINGS
# ==========================================

MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb://localhost:27017/"
)

DATABASE_NAME = os.getenv(
    "MONGODB_DATABASE",
    "sahayakai"
)


# ==========================================
# CREATE MONGODB CLIENT
# ==========================================

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)


# ==========================================
# DATABASE
# ==========================================

db = client[DATABASE_NAME]


# ==========================================
# COLLECTIONS
# ==========================================

schemes_collection = db["schemes"]

users_collection = db["users"]

documents_collection = db["documents"]

chats_collection = db["chats"]


# ==========================================
# DATABASE CONNECTION TEST
# ==========================================

def test_database_connection():

    try:

        client.admin.command("ping")

        return True

    except Exception as error:

        print(
            "MongoDB connection error:",
            error
        )

        return False