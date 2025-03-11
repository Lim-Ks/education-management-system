from sharedfunction import *

#view profile
def view_profile(student_name):
    students = load_data_file("data/student.txt")
    for student in students:
        if student["name"] == student_name:
            print("Student Profile")
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course_id']}")
            print(f"Phone: {student['phone_num']}")
            print(f"Emergency Contact: {student['emergency_num']}")


def add_student():
    students = load_data_file("data/student.txt")    #load student.txt
    for number, data in enumerate(students):
        if number == len(students)-1:
            student_id = data["student_id"]
    student_id_number = int(student_id.replace("S","")) +1
    new_student_id = f"S{student_id_number}"
    student_name = str(input("Enter your name: "))
    student_age = str(input("Enter your age: "))
    student_password = str(input("Enter your password: "))
    phone_num = str(input("Enter your phone number: "))
    emergency_num = str(input("Enter emergency contact number: "))
    if not student_name or not student_age or not student_password or not phone_num or not emergency_num:
        print("Data cannot be blank!")
        return
    new_student = ({"student_id": new_student_id, "name": student_name, "age": student_age,
                     "course_id": [] , "phone_num": phone_num, "emergency_num": emergency_num,
                    "enrollment_status":"undone","status": "registered"})
    students.append(new_student)    #add new data
    save_data_file("data/student.txt", students)  #save new data to student.txt
    add_user(student_name,"student",student_password)
    print("Student account created.")


def enroll_course(student):
    students = load_data_file("data/student.txt")  # Load student.txt
    courses = load_data_file("data/course.txt")  # Load course.txt
    print("Available Courses:")
    for course in courses:
        print(f"{course['course_id']} : {course['course_name']} - {course['teacher']}")
    course_id = str(input("Enter Course ID to enroll: "))

    valid_course = []  #set to []
    for course in courses:
        if course["course_id"] == course_id:
            valid_course = course  #store the found course
            break  #exit loop once found
    if valid_course == []:
        print("Invalid course ID.")
        return
    for enrolled in students:
        if enrolled["student_id"] == student["student_id"]:
            if course_id in enrolled["course_id"]:
                print(f"You are already enrolled in {course_id}.")
                return
            enrolled["course_id"].append(course_id)
            save_data_file("data/student.txt", students)  #save to student txt
            print(f"Successfully enrolled.")
            return


#check grades
def check_grades(student):
    grades = load_data_file("data/grade.txt")    #load grades.txt
    #only the specific student grades
    student_grades = [grade_record for grade_record in grades if grade_record["student_id"] == student["student_id"]]
    if student_grades:  #check for grades
        for grade in student_grades:
            print("Your Grades")
            print(f"Course: {grade['course_id']} ")
            print(f"Assignment Grade: {grade['assignment_grade']}")
            print(f"Exam Grade: {grade['exam_grade']}")
            print(f"Teacher's review: {grade['feedback']}")
    else:
        print("No grades available.")


#submit feedback
def submit_feedback(student):
    feedbacks = load_data_file("data/feedback.txt")  #load feedbacks.txt
    course_id = str(input("Enter Course ID for feedback: "))
    course_feedback = str(input("Enter feedback for the course: "))
    teacher_feedback = str(input("Enter feedback for the teacher: "))
    overall = str(input("Enter overall academic experiences: "))
    new_feedbacks = {"student_id": student["student_id"], "course_id": course_id, "course_feedback": course_feedback,
                     "teacher_feedback": teacher_feedback, "overall": overall}
    feedbacks.append(new_feedbacks) #add data
    save_data_file("data/feedback.txt", feedbacks)   #save data to feedbacks.txt
    print("Feedback submitted.")


#access materials
def access_materials(student):
    materials = load_data_file("data/material.txt")  #load material.txt
    student_courses = student["course_id"]    # check enrolled courses
    for material in materials:  #loop through file
        if material["course_id"] in student_courses:
            print("Course Materials")
            print(f"{material['course_id']} : {material['course_material']}")
            print(f"File: {material['material_url']}")



def update_profile(student):
    students = load_data_file("data/student.txt")  #load students.txt
    courses = load_data_file("data/course.txt")  #load courses.txt
    print("Update Profile:")
    print("Leave blank to retain current info.")
    new_student_id = str(input(f"Enter new student ID: ")) or student["student_id"]
    if new_student_id != student["student_id"]:  #check when changing ID
        if any(record["student_id"] == new_student_id for record in students):
            print("Student ID exists.")
            return  #end function

    new_name = str(input(f"Enter new name: ")) or student["name"]
    new_age = str(input(f"Enter new age: ")) or student["age"]
    new_num = str(input(f"Enter new phone number: ")) or student["phone_num"]
    new_emergency_num = str(input(f"Enter new emergency number: ")) or student["emergency_num"]

    print("Current Enrolled Courses:", ", ".join(student["course_id"]))
    modify_courses = str(input("Do you want to modify your courses? (yes/no): ")).lower()
    new_course_id = student["course_id"].copy()  #keep original courses
    if modify_courses == "yes":
        while True:
            print("Current Courses:", ", ".join(new_course_id))
            course_to_modify = str(input("Enter Course ID to modify (or press enter for finish): ")).strip()
            if not course_to_modify:
                break
            if course_to_modify not in new_course_id:
                print("Not enrolled in this course")
                continue    #ask agin
            modify = input(f"Replace (1) or delete (2) '{course_to_modify}'? (Enter 1 or 2): ")
            if modify == "1":  #replace course
                new_course_id = input("Enter new Course ID: ")
                valid_courses = {course["course_id"] for course in courses} #store valid course IDs
                if new_course_id not in valid_courses:
                    print("Invalid course ID.")
                    continue    #ask again
                new_course_id.remove(course_to_modify)
                new_course_id.append(new_course_id)
                print(f"Course replaced.")
            elif modify == "2":  #delete course
                new_course_id.remove(course_to_modify)
                print(f"Course removed.")
            else:
                print("Invalid choice. Please enter 1 or 2.")

    for record in students:
        if record["student_id"] == student["student_id"]:
            record["student_id"] = new_student_id
            record["name"] = new_name
            record["student_age"] = new_age
            record["course_id"] = new_course_id
            record["phone_num"] = new_num
            record["emergency_num"] = new_emergency_num
            break
    save_data_file("data/student.txt", students)  # Save to student.txt
    print("Profile updated.")


def student_menu(student_name):
    student_list = load_data_file("data/student.txt")
    for student_profile in student_list:
        if student_profile["name"] == student_name:
            student = student_profile
    while True:
        print("1. View Profile")
        print("2. Enroll in a Course")
        print("3. Check Grades")
        print("4. Submit Feedback")
        print("5. Access Course Materials")
        print("6. Update Profile")
        print("7. Logout")
        choice = str(input("Enter your choice: "))
        if choice == "1":
            view_profile(student_name)
        elif choice == "2":
            enroll_course(student)
        elif choice == "3":
            check_grades(student)
        elif choice == "4":
            submit_feedback(student)
        elif choice == "5":
            access_materials(student)
        elif choice == "6":
            update_profile(student)
        elif choice == "7":
            return
        else:
            print("Invalid choice.")
