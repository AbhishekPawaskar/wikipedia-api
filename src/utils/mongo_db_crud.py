import os
from src.connector.mongo_db_connector import MongoDBConnection
from src.datamodels.models import MongoDBHistoryModel, WikiWordHistoryResponse

database_name = os.environ.get('DATABASE_NAME')
collection_name = os.environ.get('COLLECTION_NAME')
client = MongoDBConnection().client
collection = client[database_name][collection_name]

def add_history(data:MongoDBHistoryModel):
    id = collection.insert_one(data.dict())
    if id is not None:
        return True
    else:
        return False

def find_history(userId:str, topic:str):
    history_result = collection.find_one({"userId":userId, "topic":topic})
    if history_result is not None:
        return WikiWordHistoryResponse(userId=history_result["userId"],
                                       history=history_result["result"])
    else:
        return None