from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Data model
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

# In-memory database
items_db: List[Item] = []

# GET all items
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

# GET item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

# POST - Add new item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)