from pydantic import BaseModel
from typing import Union
from typing import Optional


class category(BaseModel):
    category_id: int

class filter(BaseModel):
    views: Optional[int]
    likes: Optional[int]
    dislikes: Optional[int]