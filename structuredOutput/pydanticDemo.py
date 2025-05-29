from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):

    # name: str

    name: str = 'nitish'   # Default value for name

    age: Optional[int] = None  # Optional field with default value None

    email: EmailStr

    cgpa: float = Field(..., ge=0.0, le=10.0, description="CGPA must be between 0.0 and 10.0")



    # name: str = Field(..., description="The name of the student")
    # age: int = Field(..., ge=0, description="The age of the student, must be a non-negative integer")
    # email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$', description="The email address of the student")


student = Student(age=20, email='abc@gmail.com',cgpa = 6)  # Creating an instance of Student with age set to 20 and email
print(student)

print(dict(student)) 

print(student.model_dump_json())


