##GET method
# from fastapi import FastAPI

# app=FastAPI()
# Student = [
#    {"id": 1, "name": "Nitish"},
#    {"id": 2, "name": "Rahul"},
# ]
# @app.get("/student")
# def get_students():
#     return Student

##POSt method
# from fastapi import FastAPI
# from pydantic import BaseModel

# app=FastAPI()

# class Student(BaseModel):
#   name:str
#   age:int

# student=[]
# @app.post("/student_post")
# def create_student(students:Student):
#   student.append(students.dict())
#   return {
#     "message":"student created",
#     "student":student
#   }

##PUT method
# from fastapi import FastAPI
# from pydantic import BaseModel

# app=FastAPI()

# students={
#     1:{"name":"Samiksha", "age":19}
# }

# class Student(BaseModel):
#     name:str
#     age:int

# app.get("/")
# def student_data():
#     return students

# @app.put("/student/{student_id}")
# def update_student(student_id:int, student:Student):
#     students[student_id]=student.dict()
#     return students[student_id]

# @app.get("/update_data")
# def update_data():
#     return students

##DELETE method

