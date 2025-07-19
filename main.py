from fastapi import FastAPI, Query
from bson import ObjectId
from db import products_collection, orders_collection
from models import Product, Order
from fastapi.responses import JSONResponse
from typing import List, Optional

app = FastAPI()

@app.post("/products", status_code=201)
def create_product(product: Product):
    result = products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@app.get("/products")
def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    cursor = products_collection.find(query).skip(offset).limit(limit)
    result = []
    for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        result.append(doc)
    return result

@app.post("/orders", status_code=201)
def create_order(order: Order):
    result = orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@app.get("/orders/{user_id}")
def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    result = []
    for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        result.append(doc)
    return result
