from datetime import datetime
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")

db = client["studentCourses"]
students = db["students"]
courses = db["courses"]
enrolements = db["enrolements"]

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.route("/add_student", methods=["POST", "GET"])
def add_student():
    if request.method == "GET":
        student_id = request.get_json().get("id")
        if student_id:
            student = students.find_one({"_id": ObjectId(student_id)})
            if not student:
                return jsonify({"err": "student not found"})
            return jsonify(serialize(student))
        return jsonify({"err": "missing id"})
    else:
        data = request.get_json()
        student = {
            "name": data["name"],
            "group": data["group"]
        }
        student_id = students.insert_one(student).inserted_id
        return jsonify({"id": str(student_id)})

@app.route("/add_course", methods=["POST", "GET"])
def add_course():
    if request.method == "GET":
        course_id = request.get_json().get("id")
        if course_id:
            course = courses.find_one({"_id": ObjectId(course_id)})
            if not course:
                return jsonify({"err": "course not found"})
            return jsonify(serialize(course))
        return jsonify({"err": "missing id"})
    else:
        data = request.get_json()
        course = {
            "title": data["title"],
            "teacher": data["teacher"]
        }
        course_id = courses.insert_one(course).inserted_id
        return jsonify({"id": str(course_id)})

@app.route("/enroll", methods=["POST"])
def enroll():
    data = request.get_json()

    student = students.find_one({"_id": ObjectId(data["student_id"])})
    course = courses.find_one({"_id": ObjectId(data["course_id"])})

    if not student or not course:
        return jsonify({"err": "Invalid student or course ID"}), 400

    enrollment = {
        "student_id": data["student_id"],
        "course_id": data["course_id"],
        "student_name": student["name"],
        "course_title": course["title"],
        "grade" : data["grade"]
    }

    enrollment_id = enrolements.insert_one(enrollment).inserted_id
    return jsonify({"enrollment_id": str(enrollment_id)})

@app.route("/student_courses/<student_id>", methods=["GET"])
def student_info(student_id):
       
    student_courses = list(enrolements.find({"student_id": student_id}))

    if not student_courses:
        return jsonify({"err": "Student is not enrolled in any course"}), 404

    return jsonify([serialize(course) for course in student_courses])

if __name__ == "__main__":
    app.run(debug=True)
