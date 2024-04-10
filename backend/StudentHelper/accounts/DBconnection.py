from pymongo import MongoClient
import os


# Connection URI for MongoDB Atlas
uri = os.environ.get('MONGODB_URI')

# Create a MongoClient and connect to MongoDB Atlas
client = MongoClient(uri)

# Access the database
db = client['Student-HelperDB']  # Replace 'your_database_name' with the name of your MongoDB database

# Access the Users collection
users_collection = db['Users']

#test connection

