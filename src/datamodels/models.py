from pydantic import BaseModel
from typing import List, Tuple

class WikiWordFrequencyRequest(BaseModel):
   topic: str
   userId:str
   n_value:int

class WikiWordFrequencyResponse(BaseModel):
   result:List[Tuple]
   userId:str

class WikiWordFrequencyErrorResponse(BaseModel):
   result:str="Topic Not Found"
   userId:str
   
class WikiWordHistoryRequest(BaseModel):
   userId:str
   topic:str

class WikiWordHistoryResponse(BaseModel):
   userId:str
   history:List

class MongoDBHistoryModel(BaseModel):
   userId:str
   topic:str
   result:List[Tuple]
