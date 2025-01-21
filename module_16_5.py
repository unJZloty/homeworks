from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def get_users_template(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user_template(request: Request, user_id: Annotated[int, Path(description="ID пользователя")]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/user/{username}/{age}")
async def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
) -> User:
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[int, Path(description="User ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Username")],
    age: Annotated[int, Path(ge=18, le=120, description="Age")]
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(description="User ID")]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User not found")
