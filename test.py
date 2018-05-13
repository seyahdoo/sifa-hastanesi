#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database import *
import datetime

def run_test():

    client.drop_database(DATABASE_NAME)


    # add some users
    user1 = {
        "phone_number": "05062609999",
        "email": "testerahmet@seyahdoo.com",
        "password": "1234",
        "first_name": "ahmet",
        "last_name": "tester",
        "role": "patient"
    }
    user1_id = users.insert_one(user1).inserted_id

    user2 = {
        "phone_number": "05062601111",
        "email": "testeryilmaz@seyahdoo.com",
        "password": "1234",
        "first_name": "yilmaz",
        "last_name": "tester",
        "role": "doctor"
    }
    user2_id = users.insert_one(user2).inserted_id

    add_user("recai","deli","testerrecai@seyahdoo.com","4321","05062604798")


if __name__ == "__main__":

    run_test()
