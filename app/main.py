from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import post, user


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome!! Social Media API Developed BY Jah-Wilson"}
