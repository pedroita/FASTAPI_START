from typing import Union
from enum import Enum
from fastapi import FastAPI


class ModelName( str, Enum):
    
    alexnet = "alexnet"
    resetnet = "resetnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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