from app import app, db
from flask import request, jsonify
from app.models.database import Student
from app.models.marshmallow import StudentSchema


# Init Schema
student_schema = StudentSchema(strict=True)
students_schema = StudentSchema(many=True, strict=True)


# Create Student
@app.route("/api/student", methods=["POST"])
def add_student():

    name = request.json["name"]
    email = request.json["email"]
    address = request.json["address"]
    phone = request.json["phone"]

    new_student = Student(name, email, address, phone)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)


# Get all Students
@app.route("/api/student/", methods=["GET"])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result.data)


# Get single Student
@app.route("/api/student/<id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)


# Update Student
@app.route("/api/student/<id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    name = request.json["name"]
    email = request.json["email"]
    address = request.json["address"]
    phone = request.json["phone"]

    student.name = name
    student.email = email
    student.address = address
    student.phone = phone

    db.session.commit()

    return student_schema.jsonify(student)


# Delete Student
@app.route("/api/student/<id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)
