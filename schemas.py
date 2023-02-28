from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class TweetSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    desc: Optional[str]=None
    date: Optional[date]=None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
    
class RequestTweet(BaseModel):
    title: str
    desc: str

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]