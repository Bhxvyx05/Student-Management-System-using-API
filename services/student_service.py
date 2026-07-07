from database.database_connection import load_mongo
from bson import ObjectId
# import requests


mongo_client = load_mongo()

database = mongo_client["student_db"]

student_collection = database["students"]

# CREATE
def create_student_service(student):

    student_collection.insert_one(student)
    # TIP
    # How to know if the above code will crash or any code will get crash and how we can fix it
    # SO WE USE TRY AND EXCEPT IN SUCH CASES AND OTHER CASES TOO TO SOLVE THE ISSUE
    # TO GET THE HABIT TO USE THIS EXCEPTION AT ALL THE PLACES SO THAT IT GETS EASY TO RESOLVE IF ANY ERROR OCCURS

    return {
        "message": "Student Added Successfully"
    }


# READ
def get_students_service():

    students = []

    data = student_collection.find()

    for student in data:

        student["_id"] = str(student["_id"])
        # THIS IS MAINLY USED FOR THE CONVERTING INTO OBJECTID - NORMAL STRING

        students.append(student)

    return students

def get_student_by_id(student_id):
    data = student_collection.find_one({"_id": ObjectId(student_id)})
    try:
        if(data is not None):
            name = data["name"]
        else:
            return {"message": "Received empty response for student_id from mongo db"}
    except Exception as e:
        print(f"Error Occurred while extracting name for student_id: {student_id}, error: {e}")
        return {"message": "Error Occurred while extracting name for student_id"}

    return name



# UPDATE
def update_student_service(student_id, updated_data):

    student_collection.update_one(
        {"_id": student_id},
        {"$set": updated_data}
    )

    return {
        "message": "Student Updated Successfully"
    }


# DELETE
def delete_student_service(student_id):

    student_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    return {
        "message": "Student Deleted Successfully"
    }
#
# def get_student_followers(student_insta_id):