from fastapi import FastAPI
app= FastAPI()

@app.get('/')
def home():
    return{"message":"This is my FastApi app"}

@app.get('/view')
def view():
    student= [
        {
        "id":1,
         "name":"Nitish",
         "age":23,
        "course":"BSCDS"},
        {
            "id":2,
            "name":"yash",
            "age":21,
            "course":"BSCDS"
        }
    ]
    return student