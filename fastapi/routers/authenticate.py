from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from ..model import Users
from ..database import SessionLocal

router = APIRouter()


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool
    role: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/auth')
def auth():
    return {'message': 'Authentication Successful'}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=create_user_request.password,
        is_active=True,
        role=create_user_request.role,
    )

    db.add(create_user_model)
    db.commit()
