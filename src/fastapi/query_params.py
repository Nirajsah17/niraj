from fastapi import FastAPI

app  = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def read_products(product_id: int, details: bool = False):
    return {"product_id": product_id, "details": details}