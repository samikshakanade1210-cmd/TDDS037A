from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
 
app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    age:int
    
students=[
    Student(id=1, name="Rahul", age=20),
    Student(id=2, name="Priya", age=19),
    Student(id=3, name="Sam", age=21)
]

@app.post("/student")
def create_student(students:Student):
    Student.append(Student.dict())
    return{
         "message":"Student created",
         "Student":students
    
}
    

@app.get("/student")
def student():
    return students

