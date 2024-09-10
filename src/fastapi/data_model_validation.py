from fastapi import FastAPI

# Data model validation using Pydantic
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  descriptions: str = None
  price: float
  tax: float = None

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}
  
@app.post("/items/")
def create_item(item: Item):
  print(item, type(item))
  return item.dict()