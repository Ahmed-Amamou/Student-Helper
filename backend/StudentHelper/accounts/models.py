from django.db import models
import os,pymongo 
from pymongo.errors import PyMongoError
from DBconnection import db

# # Create your models here.
# #User is a student who can register in the system and use its services, mongodb is used to store the data of the users
# #The user has the following attributes: firstName, lastName, email, password, specialization, university, year, status
# #what more should be added in this file models.py?
# #The User model should be created to store the data of the users in the Users collection in the MongoDB database.


#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     specialization = models.CharField(max_length=100)
#     university = models.CharField(max_length=100)
#     year = models.CharField(max_length=100)
#     #Status of the user means he's either verified or not   
#     status = models.BooleanField(default=False)
    

users_collection = db['Users']
users_collection.insert_one({'firstName':'Ahmed',
                             'lastName':'Amamou',
                             'email':'ahmedamamou@gmail.com',
                             'password':'123456',
                             'specialization':'Computer Science',
                             'university':'University of Sfax',
                             'year':'Second',
                             'status':False})

