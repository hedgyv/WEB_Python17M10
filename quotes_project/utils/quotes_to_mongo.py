import json
from bson.objectid import ObjectId


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://web17_mod8:IDkrkN1JmruWcbSb@web17.k2uu2ec.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.quotes_db

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
    
for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote' : quote['quote'],
            'tags' : quote['tags'],
            'author' : ObjectId(author['_id'])
        })