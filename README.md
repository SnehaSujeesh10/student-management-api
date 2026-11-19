# Student Management API

## Project Description
A simple Student Management API built using Python and FastAPI.

This application allows users to add, view, search, and delete student records.

## Technologies Used
- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Features
- Add a new student
- View all students
- Search students using roll number
- Delete student records
- Validate student information
- Handle errors for duplicate and missing students

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home |
| POST | `/students` | Add student |
| GET | `/students` | View all students |
| GET | `/students/{roll_no}` | Search student |
| DELETE | `/students/{roll_no}` | Delete student |

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to access the API documentation.

## Run Tests

```bash
pytest -v
```

## Testing
All 6 automated tests passed successfully.
