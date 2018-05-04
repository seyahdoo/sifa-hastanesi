from pymongo import MongoClient
import datetime

DATABASE_NAME = "issue-tracker"

client = MongoClient()

db = client[DATABASE_NAME]

users = db.users
appointments = db.appointments


if __name__ == "__main__":

    user = {"author": "mikey",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}


    #post_id = posts.insert_one(post).inserted_id

    #print(post_id)
