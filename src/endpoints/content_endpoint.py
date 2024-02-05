
from src.datamodels.models import (
   WikiWordFrequencyRequest,
   WikiWordFrequencyResponse,
   WikiWordFrequencyErrorResponse,
   WikiWordHistoryRequest,
   WikiWordHistoryResponse,
   MongoDBHistoryModel
)
from src.utils.content_extractor import get_content_frequency
from src.utils.mongo_db_crud import add_history, find_history

def word_frequency_analysis(request_body:WikiWordFrequencyRequest):
    try:
        history = find_history(userId=request_body.userId, 
                               topic=request_body.topic)
        if history is not None:
            return WikiWordFrequencyResponse(result=history.history,
                                             userId=history.userId)
        else:
            result = get_content_frequency(topic=request_body.topic,
                                        n_value=request_body.n_value)
            ack = add_history(data= MongoDBHistoryModel(userId=request_body.userId,
                                                        topic=request_body.topic,
                                                        result=result))
            return WikiWordFrequencyResponse(result=result,
                                            userId=request_body.userId)
    except Exception as e:
        return WikiWordFrequencyErrorResponse(userId=request_body.userId)

def search_history(request_body:WikiWordHistoryRequest):
    try:
        history = find_history(userId=request_body.userId, 
                               topic=request_body.topic)
        if history is not None:
            return history
        else:
            return WikiWordHistoryResponse(userId=request_body.userId,history=[])
    except Exception as e:
        return WikiWordHistoryResponse(userId=request_body.userId,history=[])

