# ==========================================
# SAHAYAKAI - USER SERVICE
# ==========================================

from app.repository.user_repository import UserRepository


repository = UserRepository()


def create_user(user_data):

    return repository.create_user(user_data)


def get_user(user_id):

    return repository.get_user(user_id)


def get_all_users():

    return repository.get_all_users()