from pydantic import BaseModel


class UserProfile(BaseModel):

    age: int

    gender: str

    occupation: str

    annual_income: int

    citizenship: str

    state: str = ""

    caste: str = ""

    religion: str = ""

    bpl: bool

    farmer: bool

    student: bool

    disabled: bool

    widow: bool

    senior_citizen: bool