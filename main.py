# Save as main.py
# from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response
import uvicorn

app = FastAPI()

# Define the data structure you expect using Pydantic
class User(BaseModel):
    username: str
    email: str
    age: int = None

# app.middleware()
# @app.middleware("http")
# async def validate_api_token(request: Request, call_next):
#     response = await call_next(request)
#     return response



@app.post("/users/")
def create_user(user: User):
    # FastAPI automatically validates that 'user' fits the User class
    return {"message": f"User {user.username} created successfully", "data": user}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,workers=4)