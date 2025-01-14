from fastapi import FastAPI, Path
from typing import Annotated

users = {"1": "Имя: Andrew, возраст: 18"}

app = FastAPI()

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]):
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
