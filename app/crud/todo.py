from sqlalchemy.orm import Session
from ..models.todo import Todo
from ..schemas.todo import TodoCreate, TodoUpdate

def get_todos(db: Session, skip: int = 0, limit: int = 100, user_id: int = None):
    query = db.query(Todo)
    if user_id:
        query = query.filter(Todo.owner_id == user_id)
    return query.offset(skip).limit(limit).all()

def create_user_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo: TodoUpdate, todo_id: int):
    db_todo = get_todo(db, todo_id=todo_id)
    update_data = todo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id=todo_id)
    db.delete(db_todo)
    db.commit()
    return db_todo