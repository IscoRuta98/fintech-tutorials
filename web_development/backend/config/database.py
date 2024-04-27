from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test1234!@cluster.cp5k1iw.mongodb.net/?retryWrites=true&w=majority&appName=cluster")

db = client.todo_db

collection_name = db["todo_collection"]