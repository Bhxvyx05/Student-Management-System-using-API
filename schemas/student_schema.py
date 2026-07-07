from typing import List

from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    subjects: List[str]