#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import *
import datetime

if __name__ == "__main__":

    client.drop_database(DATABASE_NAME)

    # patients
    add_user("ali","tester","ali@seyahdoo.com","123","05062605000","patient")
    add_user("veli","tester","veli@seyahdoo.com","123","05062600400","patient")
    add_user("recai","deli","recai@seyahdoo.com","123","05062604798")

    # doctors
    add_user("yılmaz","doktor","yılmaz@seyahdoo.com","123","05062600300","doctor")
    add_user("hatice","hemşire","hatice@seyahdoo.com","123","05062600100","doctor")
    add_user("vurdumduymaz","eleman","vurdumduymaz@seyahdoo.com","123","05062600100","doctor")
