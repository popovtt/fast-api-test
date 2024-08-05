import uvicorn
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

from items_views import router as items_router

app = FastAPI()
app.include_router(items_router)


class CreateUser(BaseModel):
    email: EmailStr
    name: str


@app.get("/")
def hello_index():
    return {"success": 200, "msg": "Hello World"}


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
