from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    name: str
    description: str
    price: float
    size: str
    tags: List[str]

class ProductOut(Product):
    id: str

class Order(BaseModel):
    user_id: str
    products: List[str]
    total_price: float

class OrderOut(Order):
    id: str
