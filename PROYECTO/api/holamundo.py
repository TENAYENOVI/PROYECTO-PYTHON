from fastapi import FastAPI
app = FastAPI() 

@app.get("/")
def raiz():
    return{"Hello": "World"}

@app.get("/items/{item_id}/{m}")
def readItem(item_id: int, m: str=None):
    return{"item_id": item_id, "m":m}