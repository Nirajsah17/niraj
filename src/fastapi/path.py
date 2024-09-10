from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_items(item_id: int, q: str = None):
  return {"items_id": item_id, q: q}