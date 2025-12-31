from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user import UserCreate, UserRead, credentials
from app.crud.users import get_user_by_email, create_user, get_users
from app.utils.credentials import verify_password

router = APIRouter(prefix="/users", tags=["users"])

# @router.post("/", response_model=UserRead)
# def create(user: UserCreate, db: Session = Depends(get_db)):
#     if get_user_by_email(db, user.email):
#         raise HTTPException(status_code=400, detail="Email already exists")
    
#     return create_user(db, user.email, user.name)

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/login")
def verify_email(data: credentials, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)

    if not user:
        return {"verified": False, "message": "No user with that email"}

    if not verify_password(data.password, user.hashed_password, user.salt, user.iterations):
        return {"verified": False, "message": "Incorrect password"}
    
    return {"verified": True, "message": "Password correct"}

@router.post("/sign_up")
def sign_up(data: credentials, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    
    if user:
        return {"created": False, "message": "Email already exists"}
    
    create_user(db, data.email, "pissname", data.password)

    return {"created": True, "message": "Account creation Succesful"}
    


