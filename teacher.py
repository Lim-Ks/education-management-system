from sharedfunction import *
from staff import add_schedule

def enroll_student():
    data_student = load_data_file("data/student.txt")
    data_course = load_data_file("data/course.txt")
    course_id = str(input("Enter course id:"))
    student_id = str(input("Enter student id:"))
    student_name = str(input("Enter student name:"))

    exists = any(
        student["student_id"] == student_id and
        course["course_id"] == course_id
        for student in data_student
        for course in data_course)
    if not exists:
        print("Invalid student id or course id.")
        return

    for student in data_student:
        if student["student_id"] == student_id:
            for course in student["course_id"]:
                if course == course_id:
                    print(f"Student {student_id},{student_name} is already enrolled in course {course_id}.")
                    return
                else:
                    student["course_id"].append(course_id)
                    save_data_file("data/student.txt", data_student)
                    print(f"Student {student_id},{student_name} is successfully enroll in course {course_id}.")
                    return

    print(f"Student {student_id},{student_name} not found.")


def add_material():
    data_material = load_data_file("data/material.txt")
    data_course = load_data_file("data/course.txt")

    course_id = str(input("Enter course id:"))
    material = str(input("Enter material:"))
    pdf = str(input("Enter pdf:"))

    exists = any(course["course_id"] == course_id for course in data_course)
    if not exists:
        print("Invalid course id.")
        return
    if material and pdf:
        new_material = {"course_id": course_id,"course_material": material,"material_url": pdf}
        data_material.append(new_material)
        save_data_file("data/material.txt",data_material)
    else:
        print("material name and url cannot be blank")
        return

#remove student course
def remove_student():
    data = load_data_file("data/student.txt")
    student_id = str(input("Enter the student id:"))
    course_id = str(input("Enter course id:"))
    exists = any(student["student_id"] == student_id for student in data)
    if not exists:
        print("Please enter a valid student id.")
        return
    for student in data:
        if student["student_id"] == student_id:
            for course in student["course_id"]:
                if course == course_id:
                    student["course_id"].remove(course_id)
                    save_data_file("data/student.txt",data)
                    print(f"Course {course_id} is removed from student {student_id}.")
                    return
                else:
                    print(f"Course {course_id} not found.")
                    return

    print(f"Student {student_id} not found.")

def grade():
    data_grade = load_data_file("data/grade.txt")
    data_student = load_data_file("data/student.txt")
    try:
        student_id = str(input("Enter student id:"))
        course_id = str(input("Enter course id:"))
        exam_score = int(input("Enter exam score:"))
        asg_score = int(input("Enter assignment score:"))
        feedback = str(input("Enter feedback:"))
        found = False
        for student in data_student:
            if student["student_id"] == student_id:
                for student_course in student["course_id"]:
                    if student_course == course_id:
                        found = True
        if not exam_score or not asg_score or not feedback:
            print("data cannot be blank")
            return
        if found == True:
            if exam_score <= 50:
                exam_grade = "A"
            elif exam_score >= 30:
                exam_grade = "B"
            elif exam_score >= 20:
                exam_grade = "C"
            elif exam_score >= 10:
                exam_grade = "D"
            else:
                exam_grade = "F"

            if asg_score <= 50:
                asg_grade = "A"
            elif asg_score >= 30:
                asg_grade = "B"
            elif asg_score >= 20:
                asg_grade = "C"
            elif asg_score >= 10:
                asg_grade = "D"
            else:
                asg_grade = "F"

            for student in data_grade:
                if student_id == student["student_id"] and course_id == student["course_id"]:
                    print(f"Student {student_id} already exists.")
                    return

            new_student = {"student_id": student_id, "course_id": course_id, "exam_score": exam_score, "exam_grade": exam_grade,
                           "assignment_score": asg_score,"assignment_grade": asg_grade,"feedback": feedback}
            data_grade.append(new_student)
            save_data_file("data/grade.txt", data_grade)
            print(f"Student {student_id} added.")
            print(f"Student {student_id} exam_score: {exam_score}")
            print(f"Student {student_id} exam_grade: {exam_grade}")
            print(f"Student {student_id} assignment_score: {asg_score}")
            print(f"Student {student_id} assignment_grade: {asg_grade}")
            print(f"Feedback:{feedback}")
        elif found == False:
            print("student or course not found")
    except ValueError:
        print("Please enter a valid input")


def attendance_tracking():
    data_attendance = load_data_file("data/attendance.txt")
    data_student = load_data_file("data/student.txt")
    data_course = load_data_file("data/course.txt")

    student_id = str(input("Enter student id:"))
    course_id = str(input("Enter course id:"))
    attendance_date = str(input("Enter date:"))

    found = False
    for student in data_student:
        if student["student_id"] == student_id:
            for student_course in student["course_id"]:
                if student_course == course_id:
                    found = True
    if found == True:
        valid_status = ["absent","present"]
        status = str(input("Enter attendance status(absent/present):"))

        if status.lower() not in valid_status:
            print("Invalid status. Please enter 'present' or 'absent'.")
            return

        for record in data_attendance:
            if record["student_id"] == student_id and record["course_id"] == course_id and record["date"] == attendance_date:
                print(f"Attendance record for student {student_id} on {attendance_date} is already exists.")
                return

        new_record = {"student_id": student_id,"course_id": course_id,"date": attendance_date,"status": status.lower()}
        data_attendance.append(new_record)
        save_data_file("data/attendance.txt",data_attendance)
        print(f"Attendance recorded: {student_id} was {status} on {attendance_date}.")
    if found == False:
        print("student or course not found")


def manage_schedule():
    while True:
        schedule_list =load_data_file("data/schedule.txt")
        course_list =load_data_file("data/course.txt")
        try:
            user_input = int(input("==== Schedule Management ====\n1)view schedule\n2)change data\n3)create schedule\n4)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if user_input == 1:
            for schedule in schedule_list:
                for course in course_list:
                    if course["course_id"] == schedule["course_id"]:
                        print("------------")
                        print("schedule id: ", schedule["schedule_id"])
                        print("course name: ", course["course_name"])
                        print("date: ", schedule["date"])
                        print("duration: ", schedule["time"])
                        print("location: ", schedule["location"])
                        print("------------")
        elif user_input == 2:
            wrong_data = str(input("Enter the schedule id that you want to change"))
            found = False
            for schedule in schedule_list:
                if wrong_data == schedule["schedule_id"]:
                    found = True
                    wrong_key = str(input("course_id, date, time, location\nEnter the data name: "))
                    correct_value = str(input("Enter the correct data: "))
                    if wrong_key not in ["course_id", "date", "time", "loaction"]:
                        print("Invalid Key")
                        continue
                    if wrong_key == "course_id":
                        exists = any(course["course_id"] == correct_value for course in course_list)
                        if not exists:
                            print("Please enter a valid course id.")
                            continue
                    if correct_value:
                        schedule[wrong_key] = correct_value
                        save_data_file("data/schedule.txt", schedule_list)
                        print("update successfully")
                    else:
                        print("correct data cannot be empty")
            if found == False:
                print("Schedule not found")
                continue
        elif user_input == 3:
            add_schedule()
        elif user_input == 4:
            break
        else:
            print("please enter a valid number")

def report_generation():
    while True:
        report_list = load_data_file("data/report.txt")
        grade_list = load_data_file("data/grade.txt")
        student_list = load_data_file("data/student.txt")
        attendance_list = load_data_file("data/attendance.txt")
        course_list = load_data_file("data/course.txt")
        try:
            admin_input = int(input("===== Report Generation =====\n1)view report\n2)update report\n3)add report\n4)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        with open("data/report.txt", "r") as file:
            reports = json.load(file)
        if admin_input == 1:
            for report in report_list:
                print("------------")
                print("student id: ", report["student_id"])
                print("name: ", report["name"])
                print("course: ", report["course"])
                print("grade: ", report["grade"])
                print("attendance: ",report["attendance"])
                print("teacher review: ",report["teacher_review"])
                print("------------")
        elif admin_input == 2:
            student_id =str(input("Enter the student id that you want to update: "))
            exists = any(student["student_id"] == student_id for student in student_list)
            if not exists:
                print("Please enter a valid student id.")
                continue
            found = False
            for report in report_list:
                if student_id == report["student_id"]:
                    found = True
                    change_report = report
                    wrong_key = str(input("course, grade, attendance, teacher review\nEnter the data type that need to update: "))
                    if wrong_key not in ["course", "grade", "attendance", "teacher review"]:
                        print("Please enter a valid data type")
                        continue
                    correct_value = str(input("Enter the correct data:"))
                    if correct_value:
                        change_report[wrong_key] = correct_value
                        save_data_file("data/report.txt", report_list)
                        print("update successfully")
            if found == False:
                print(f"{student_id} report not found")
        elif admin_input == 3:
            student_id = str(input("Enter the student id: "))
            course_id =str(input("Enter the course id: "))
            teacher_review = str(input("Enter the teacher review: "))
            exists = any(
                student["student_id"] == student_id and
                course["course_id"] == course_id
                for student in student_list
                for course in course_list)
            if not exists:
                print("Invalid student id or course id.")
                continue
            for grade in grade_list:
                if student_id == grade["student_id"]:
                    if course_id == grade["course_id"]:
                        total_score = grade["exam_score"]+grade["assignment_score"]
            if total_score >= 90:
                final_grade = "A+"
            elif total_score >=80:
                final_grade = "A"
            elif total_score >=70:
                final_grade = "A-"
            elif total_score >=60:
                final_grade = "B+"
            elif total_score >= 50:
                final_grade = "B"
            elif total_score >= 40:
                final_grade = "C"
            elif total_score >= 30:
                final_grade = "D"
            elif total_score >= 20:
                final_grade = "E"
            else:
                final_grade ="F"
            total_class = 0
            total_present = 0
            for attendance in attendance_list:
                if student_id == attendance["student_id"]:
                    if course_id == attendance["course_id"]:
                        total_class+=1
                        if attendance["status"] == "present":
                            total_present+=1
            attendance = f"{int(total_present/total_class*100)}%"
            for student in student_list:
                if student["student_id"] == student_id:
                    student_name = student["name"]
            for course in course_list:
                if course_id == course["course_id"]:
                    course_name = course["course_name"]
            new_report = {"student_id": student_id, "name": student_name, "course": course_name, "grade": final_grade, "attendance": attendance,"teacher_review":teacher_review}
            report_list.append(new_report)
            save_data_file("data/report.txt",report_list)
        elif admin_input == 4:
            break
        else:
            print("please enter a valid number")

def teacher():
    while True:
        print("\n===== Teacher Management System =====")
        print("1. Course Creation and Management")
        print("2. Student Enrollment")
        print("3. Grading and Assessment")
        print("4. Attendance Tracking")
        print("5. Report Generation")
        print("6. Add Material")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            print("===== Course Creation and Management =====")
            print("1. Manage Course")
            print("2. Manage Schedule")


            try:
                course = int(input("Enter your choice (1-2): "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue

            if course == 1:
                course_management()
            elif course == 2:
                manage_schedule()
            else:
                print("Invalid choice. Try again.")

        elif choice == 2:
            print("===== Student Enrollment =====")
            print("1. Enroll Student")
            print("2. Remove Student")

            try:
                student = int(input("Enter your choice (1-2): "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue

            if student == 1:
                enroll_student()
            elif student == 2:
                remove_student()
            else:
                print("Invalid choice. Try again.")

        elif choice == 3:
            print("===== Grading and Assessment =====")
            grade()

        elif choice == 4:
            print("===== Attendance Tracking =====")
            attendance_tracking()

        elif choice == 5:
            report_generation()

        elif choice == 6:
            print("===== Add Material =====")
            add_material()

        elif choice == 7:
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")