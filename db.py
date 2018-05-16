#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import datetime

DATABASE_NAME = "sifa-hastanesi"

client = MongoClient()

db = client[DATABASE_NAME]

users = db.users
appointments = db.appointments


def add_user(
        first_name,
        last_name,
        email,
        password,
        phone_number,
        role = "patient"):
"""Add a user to database"""

    u = {
        "phone_number": phone_number,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "role": role
    }
    user_id = users.insert_one(u).inserted_id

    return user_id
