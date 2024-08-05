import uvicorn
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel
from typing import Annotated


app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr
    name: str


@app.get("/")
def hello_index():
    return {"success": 200, "msg": "Hello World"}


@app.get("/items/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id
        },
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
        "name": user.name,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
