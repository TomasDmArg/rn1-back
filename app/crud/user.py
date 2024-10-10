from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from ..auth.jwt_handler import AuthHandler

auth_handler = AuthHandler()

def get_user(db: Session, user_id: int):
    """Retrieve a user by id."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """Retrieve a user by email."""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """Create a new user."""
    hashed_password = auth_handler.get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user