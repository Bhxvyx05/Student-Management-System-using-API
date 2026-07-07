from urllib import response

from fastapi import APIRouter

from schemas.student_schema import Student

from services.student_service import (
    create_student_service,
    get_students_service,
    update_student_service,
    delete_student_service
)

router = APIRouter()

# CREATE
@router.post("/students")
def create_student(student: Student):
    def create_student(student: Student):
        # This means the incoming request body must match the StudentCreate schema.
        # So FastAPI will check the data before the function continues
        response = create_student_service(
            student.model_dump() # converts the Pydantic object into a normalPythondictionary.
        )
        return response



# READ
@router.get("/students")
def get_students():

    response = get_students_service()

    return response


# UPDATE
@router.put("/students/{student_id}")

# PATH PARAMETER
# "/students/{student_id}"
# dynamic student id from URL

def update_student(student_id: str, student: Student):

    response = update_student_service(
        student_id,
        student.model_dump()
    )

    return response


# DELETE
@router.delete("/students/{student_id}")
def delete_student(student_id: str):

    response = delete_student_service(student_id)

    return response