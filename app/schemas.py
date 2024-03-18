from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    department: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    

