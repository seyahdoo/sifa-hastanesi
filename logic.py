from database import *


def add_user(
        first_name,
        last_name,
        email,
        password,
        phone_number):

    u = {
        "phone_number": phone_number,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "role": "patient"
    }
    user_id = users.insert_one(u).inserted_id

    return user_id
