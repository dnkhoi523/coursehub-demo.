students = [
    {"id": "22000001", "name": "Nguyen Minh Anh", "major": "KHDL"},
    {"id": "22000002", "name": "Tran Duc Long", "major": "KHDL"},
]
courses = [
    {
        "code": "INT2204",
        "name": "Co so du lieu Web va he thong thong tin",
        "capacity": 3,
        "enrolled": 2,
    },
    {
        "code": "INT2205",
        "name": "Khai pha du lieu",
        "capacity": 2,
        "enrolled": 2,
    },
]
enrollments = [
    {"student_id": "22000001", "course_code": "INT2204"}
]

def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return True
    return False

def find_course(course_code):
    for course in courses:
        if course["code"] == course_code:
            return True
    return False

def is_course_full(course_code):
    remaining = 0
    for course in courses:
        if course["code"] == course_code:
            remaining = course["capacity"] - course["enrolled"]
    if remaining <= 0:
        return True
    return False

def is_student_enrolled(student_id, course_code):
    for enrollment in enrollments:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            return True
    return False

def enroll_student(student_id, course_code):
    if not find_student(student_id):
        print("Student not found")
    elif not find_course(course_code):
        print("Course not found")
    elif is_course_full(course_code):
        print("Course is full")
    elif is_student_enrolled(student_id, course_code):
        print("Student is already enrolled in this course")
    else:
        enrollments.append({"student_id": student_id, "course_code": course_code})
        print("Enrollment successful")

student_id = input("Enter student ID: ")
course_code = input("Enter course code: ")
enroll_student(student_id, course_code)