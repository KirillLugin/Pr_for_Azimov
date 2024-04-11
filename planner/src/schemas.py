from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: int
    description: str

class CreateUser(BaseModel):
    name: str
    fullnane: str
    nickname: Optional[str]

class ReadUser(CreateUser):
    id: str
    name: str
    fullnane: str
    nickname: Optional[str]
