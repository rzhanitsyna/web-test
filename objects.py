import typing

from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')


class List(BaseModel, Generic[T]):
    items: List[T]


class Error(BaseModel):
    code: str
    id: float
    message: str
    data: Optional[typing.Any]


class Response(BaseModel, Generic[T]):
    result: T
    error: Optional[Error]


class University(BaseModel):
    _id: str
    name: str
    serviceName: str
    referenceDate: int
    # referenceWeek: Union[]


class SchedUser(BaseModel):
    _id: str
    name: str
    university: University


class User(BaseModel):
    _id: str
    firstName: str
    lastName: str
    avatar: str
    serviceLogin: str
    vkId: int
    isAdsEnabled: bool
    hasCards: bool
    university: University
    scheduleUser: SchedUser
