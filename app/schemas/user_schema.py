from pydantic import BaseModel


class UserProfile(BaseModel):
    age: int
    gender: str
    state: str
    occupation: str
    income: int
    category: str