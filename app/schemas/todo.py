from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    """Base Todo schema with common attributes."""
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    """Schema for todo creation."""
    pass

class TodoUpdate(TodoBase):
    """Schema for todo update, allowing completed status to be changed."""
    completed: Optional[bool] = None

class Todo(TodoBase):
    """
    Full Todo schema, used for responses.
    Includes id, completed status, and owner id.
    """
    id: int
    completed: bool
    owner_id: int

    model_config = {
        "from_attributes": True
    }