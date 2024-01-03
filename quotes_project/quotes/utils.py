from pymongo import MongoClient

def get_mongodb():
    
    uri = "mongodb+srv://web17_mod8:IDkrkN1JmruWcbSb@web17.k2uu2ec.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.quotes_db
    
    return db