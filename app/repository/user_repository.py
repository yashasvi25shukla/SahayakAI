# ==========================================
# SAHAYAKAI - USER REPOSITORY
# ==========================================

from datetime import datetime
from app.database.db import users_collection


class UserRepository:

    # ==========================================
    # CREATE USER
    # ==========================================

    def create_user(self, user_data):

        data = user_data.copy()

        data["created_at"] = datetime.utcnow()

        result = users_collection.insert_one(data)

        return str(result.inserted_id)

    # ==========================================
    # GET USER BY ID
    # ==========================================

    def get_user(self, user_id):

        from bson import ObjectId

        try:

            user = users_collection.find_one(
                {"_id": ObjectId(user_id)}
            )

            if user:

                user["_id"] = str(user["_id"])

            return user

        except Exception:

            return None

    # ==========================================
    # GET ALL USERS
    # ==========================================

    def get_all_users(self):

        users = list(
            users_collection.find(
                {},
                {"_id": 0}
            )
        )

        return users