from typing import Union
from enum import Enum
from fastapi import FastAPI,Query,Path
from pydantic import BaseModel





app = FastAPI()

class Item (BaseModel):
    name : str
    description : str | None = None
    price: float
    tax: float | None = None

class ModelName( str, Enum):
    
    alexnet = "alexnet"
    resetnet = "resetnet"
    lenet = "lenet"
    
    
fake_base = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]  

@app.get ("/")
async def root():
    return {"Bem vindo": "API ativa"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": 'o usuario é'}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return{"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
async def read_items(q: str= Query(default=None,title="Query string",description="Query de consulta",min_length=3)):
    results = {"itens ": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path (title= "The ID of the item to get"),q : str | None = Query(default=None, alias="item-query"),):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


