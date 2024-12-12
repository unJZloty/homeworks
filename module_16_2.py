from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(
    user_id: Annotated[
        int,
        Path(
            description="Enter User ID",
            ge=1,
            le=100,
            example=11
        )
    ]
):
    return {"user_id": user_id}

@app.get("/user/{username}/{age}")
def get_user_details(
    username: Annotated[
        str,
        Path(
            description="Enter username",
            min_length=5,
            max_length=20,
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            description="Enter age",
            ge=18,
            le=120,
            example=24
        )
    ]
):
    return {"username": username, "age": age}
