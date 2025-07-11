python
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def update_user(db: Session, id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return None
    for field, value in user.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True