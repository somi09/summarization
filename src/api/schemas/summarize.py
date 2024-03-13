
from pydantic import BaseModel, HttpUrl

class SummarizeWebPageRequest(BaseModel):
    url: HttpUrl
    summary_len: int

class SummarizeTextRequest(BaseModel):
    text: str
    summary_len: int

class SummarizeResponse(BaseModel):
    summary: str
    number_of_words: int