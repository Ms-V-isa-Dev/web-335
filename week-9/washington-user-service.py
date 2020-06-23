#==============================================
#; Title:  Exercise 9.2
#; Author: Verlee Washington
#; Date:   22 June 2020
#; Modified by:
#; Description: Querying and creating documents.
#;=============================================

from pymongo import MongoClient
import pprint
import datetime

client=MongoClient("localhost", 27017)
db = client.web335

user ={

    "first_name": "LooLu",
    "last_name": "Winters",
    "email": "lwinters@me.com",
    "employee_id":"0000002",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id":"0000002"}))

from pymongo import MongoClient
import pprint
client=MongoClient("localhost",27017)
db = client.web335
employee_id = "0000002"
pprint.pprint(db.users.find_one({"employee_id":employee_id}))

