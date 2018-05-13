from pymongo import MongoClient
import datetime

DATABASE_NAME = "issue-tracker"

client = MongoClient()

db = client[DATABASE_NAME]

users = db.users
appointments = db.appointments


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




if __name__ == "__main__":

    user = {"author": "mikey",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}


    #post_id = posts.insert_one(post).inserted_id

    #print(post_id)
