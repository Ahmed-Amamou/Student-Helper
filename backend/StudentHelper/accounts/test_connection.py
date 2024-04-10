from pymongo import MongoClient
from DBconnection import db
import bcrypt


#verify if the login is correct
users_collection = db['Users']
def verify_login(email, password):
    user = users_collection.find_one({'email': email})
    if user:
        if bcrypt.checkpw(password, user['password']):
            return user
        else:
            return "Incorrect password bro"
    else:
        return "User not found"
#verify if the email is already used
print(verify_login('ahmedamamou@gmail.com', b'123456'))

    

        
