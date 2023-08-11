import pymongo
import pandas as pd

#mongodb Config settings
connect_URI = pymongo.MongoClient('mongodb://localhost:27017/')

#Access my Database
mydb = connect_URI["EmployeeProfile"]
myEPP = mydb["EPP"]

try:

    #Accept input and store in database
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    job = input("Enter Job Role: ")

    employee_profile = {
        "FirstName": first_name,
        "LastName": last_name,
        "Gender": gender,
        "Age": age,
        "JobRole": job
    }
#Insert into my database
    myEPP.insert_one(employee_profile)
#Display newest update
    newest_employee = myEPP.find().sort([('$natural', -1)]).limit(1)
    print("Newest Employee Profile: ")
    for employee in newest_employee:
        print(employee)
        
           
    print("Success!")
    print('Thank you for updating!')
except pymongo.errors.PyMongoError as e:
    print("Database  update failed: ", e)
except Exception as e:
    print("Error Error---Code Error--Fix ME NOW!")
