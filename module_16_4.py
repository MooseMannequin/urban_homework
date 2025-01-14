from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id : int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> list[User]:
    print(users)
    return users

@app.post('/user/{username}/{age}')
async def add_user(user: User,
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='moose')],
        age: int = Path(ge=1, le=100, description='Enter User ID', examples=7)) -> User:

    user.id = 1 if users == [] else (1 + users[-1].id)
    user.username = username
    user.age = age
    users.append(user)
    print(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:int, username:str, age:int) -> User:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return users[user_id]
        # for user in users:
        #     if user.id == user_id:
        #         user.username = username
        #         user.age = age
        #         return users
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id:int) -> User:
    try:
        deleted_user = users[user_id]
        users.pop(user_id)
        return deleted_user
        # for user in users:
        #     if user.id == user_id:
        #         users.pop(users.index(user))
        #         print(user)
        #         return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')