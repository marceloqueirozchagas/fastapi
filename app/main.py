from fastapi import FastAPI
from .routes import auth, post, user, vote

from . import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Api is running!"}


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)

# uvicorn app.main:app --reload
