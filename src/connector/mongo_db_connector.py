import os
from pymongo import MongoClient

connection_string = os.environ.get('MONGODB_CONN_STRING')

#Singleton class implementation
class MongoDBConnection:
    _instance = None
    
    def __init__(self):
        self.client = MongoClient(connection_string)
        
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls) 
            cls._instance.__init__()
        else:
            if cls._instance.client is None or cls._instance.client.is_closed(): 
                cls._instance.client = MongoClient(connection_string)
                
        return cls._instance
    

