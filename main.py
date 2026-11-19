
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Student Management API")

students = []


class Student(BaseModel):
    roll_no: int
    name: str = Field(min_length=2)
    age: int = Field(gt=0)
    course: str


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.post("/students")
def add_student(student: Student):
    for s in students:
        if s["roll_no"] == student.roll_no:
            raise HTTPException(
                status_code=400,
                detail="Student already exists"
            )

    students.append(student.model_dump())
    return {"message": "Student added successfully"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{roll_no}")
def get_student(roll_no: int):
    for student in students:
        if student["roll_no"] == roll_no:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{roll_no}")
def delete_student(roll_no: int):
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
