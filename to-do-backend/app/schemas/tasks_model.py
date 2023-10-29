from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="id")
    user_id: int
    title: str = Field(min_length=1, max_length=50)
    description: str | None = Field(
        default=None,
        title='The description of the task',
        max_length=254,
    )
