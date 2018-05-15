#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import *
import datetime

if __name__ == "__main__":

    client.drop_database(DATABASE_NAME)

    add_user("ali","tester","ali@seyahdoo.com","123","05062605000","patient")
    add_user("veli","tester","veli@seyahdoo.com","123","05062600400","patient")
    add_user("yılmaz","tester","yılmaz@seyahdoo.com","123","05062600300","doctor")
    add_user("harici","tester","harici@seyahdoo.com","123","05062600100","doctor")
    add_user("recai","deli","testerrecai@seyahdoo.com","123","05062604798")
