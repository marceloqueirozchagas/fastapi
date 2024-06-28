from datetime import datetime
from pydantic import BaseModel, EmailStr, conint


class UserRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostRequest(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True


class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        from_attributes = True


class UserRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    id: int = None


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class VoteRequest(BaseModel):
    post_id: int
    dir: int
