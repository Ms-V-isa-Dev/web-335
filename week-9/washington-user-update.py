#==============================================
#; Title:  Exercise 9.3
#; Author: Verlee Washington
#; Date:   23 June 2020
#; Modified by:
#; Description: Updating and deleting documents.
#;=============================================

from pymongo import MongoClient
import pprint


client = MongoClient("localhost", 27017)
db = client.web335
db.users.update_one(
  {'employee_id': '0000002'},
  {
    "$set":{
      "email":"vwashington@my365.bellevue.edu"
    }
  }
)

from pymongo import MongoClient
import pprint

client = MongoClient("localhost", 27017)
db = client.web335

employee_id = "0000002"

pprint.pprint(db.users.find_one({"employee_id": "0000002"}))
