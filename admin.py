from sharedfunction import *
from teacher import *
from student import *
from staff import *

def add_user(name, role, password):
    user_list = load_data_file("data/user.txt")
    for number, data in enumerate(user_list):
        if number == len(user_list)-1:
            new_user_id = data["user_id"]+1
    new_data = {"user_id": new_user_id, "name": name, "role": role, "password": password}
    user_list.append(new_data)
    save_data_file("data/user.txt",user_list)


def generate_report():
    while True:
        report_list = load_data_file("data/report.txt")
        grade_list = load_data_file("data/grade.txt")
        student_list = load_data_file("data/student.txt")
        attendance_list = load_data_file("data/attendance.txt")
        course_list = load_data_file("data/course.txt")
        financial_list = load_data_file("data/financial report.txt")
        try:
            admin_input = int(input("===== Report Generation =====\n1)view report\n2)update report / financial report\n3)genearate report\n4)generate financial report\n5)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if admin_input == 1:
            try:
                choice = int(input("1)report\n2)financial report\nchoose the report that you want to update: "))
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            if choice not in [1,2]:
                print("please enter 1 or 2")
                continue
            elif choice == 1:
                for report in report_list:
                    print("------------")
                    print("student id: ", report["student_id"])
                    print("name: ", report["name"])
                    print("course: ", report["course"])
                    print("grade: ", report["grade"])
                    print("attendance: ",report["attendance"])
                    print("teacher review: ",report["teacher_review"])
                    print("------------")
            elif choice == 2:
                for finance in financial_list:
                    print("------------")
                    print("student id: ", finance["student_id"])
                    print("name: ", finance["name"])
                    print("total fee: ", finance["course"])
                    print("total paid: ", finance["grade"])
                    print("outstanding: ",finance["attendance"])
                    print("------------")
        elif admin_input == 2:
            try:
                choice = int(input("1)report\n2)financial report\nchoose the report that you want to update: "))
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            if choice not in [1,2]:
                print("please enter 1 or 2")
                continue
            student_id =str(input("Enter the student id that you want to update: "))
            exists = any(student["student_id"] == student_id for student in student_list)
            found = False
            if not exists:
                print("Please enter a valid student id.")
                continue
            elif choice == 1:
                for report in report_list:
                    if student_id == report["student_id"]:
                        found = True
                        change_report = report
                        wrong_key = str(input("student id, name, course, grade, attendance, teacher review\nEnter the data type that need to update: "))
                        if wrong_key not in ["student id", "name", "course","grade","attendance","teacher review"]:
                            print("Please enter a valid input")
                            continue
                        correct_value = str(input("Enter the correct data (or press Enter to remain same)")) or report[wrong_key]
                        change_report[wrong_key] =correct_value
                if found == False:
                    print(f"{student_id} report not found")
                save_data_file("data/report.txt",report_list)
            elif choice == 2:
                for finance in financial_list:
                    if student_id ==finance["student_id"]:
                        found = True
                        change_financial_report = finance
                        wrong_key = str(input("student id, name, total fee, total paid, outstanding\nEnter the data type that need to update: "))
                        if wrong_key not in ["student id", "name", "total fee","total paid","outstanding"]:
                            print("Please enter a valid input")
                            continue
                        correct_value = str(input("Enter the correct data (or press Enter to remain same)")) or finance[wrong_key]
                        change_financial_report[wrong_key] =correct_value
                if found == False:
                    print(f"{student_id} report not found")
                save_data_file("data/financial report.txt",financial_list)
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
            try:
                student_id = str(input("Enter the student id: "))
                total_fee =int(input("Enter the student total tuition fee: "))
                total_paid =int(input("Enter the total that student paid"))
                outstanding = total_fee-total_paid
            except ValueError:
                print("Invalid input")
                continue
            exists = any(student["student_id"] == student_id for student in student_list)
            if not exists:
                print("Invalid student id.")
                continue
            for student in student_list:
                if student["student_id"] == student_id:
                    student_name = student["name"]
            new_financial_report ={"student_id":student_id,"name":student_name,"total_fee":total_fee,"total_paid":total_paid,"outstanding":outstanding}
        elif admin_input == 5:
            break
        else:
            print("please enter a valid number")


def student_management():
    while True:
        student_list = load_data_file("data/student.txt")
        grade_list = load_data_file("data/grade.txt")
        try:
            choice = int(input("==== Student Management ====\n1) view student\n2) update student profile\n3) view student grade\n4) exit\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            for student in student_list:
                print("------------")
                print("student id: ", student["student_id"])
                print("name: ", student["name"])
                print("age: ", student["age"])
                print("course id: ", ", ".join(student["course_id"]))
                print("phone number: ", student["phone_num"])
                print("emergency number: ", student["emergency_num"])
                print("enrollment status: ",student["enrollment_status"])
                print("status: ",student["status"])
                print("------------")
        elif choice == 2:
            try:
                wrong_key = input("enter the data key that you want to change: ")
                wrong_value = input("enter the data that you want to change: ")
                correct_value = input("enter the correct data: ")
                exists = any(student[wrong_key] == wrong_value for student in student_list)
                if not exists:
                    print("Please enter a valid input.")
                    continue
                change_data("data/student.txt", wrong_key, wrong_value, correct_value)
            except KeyError:
                print("Please enter a valid input")
                continue
        elif choice == 3:
            for grade in grade_list:
                print("------------")
                print("student id: ", grade["student_id"])
                print("name: ", grade["course_id"])
                print("exam score: ", grade["exam_score"])
                print("exam grade: ", (grade["exam_grade"]))
                print("assignment score: ", grade["assignment_score"])
                print("eassignment grade: ", grade["assignment_grade"])
                print("teacher feedback: ", grade["feedback"])
                print("------------")
        elif choice == 4:
            break


def manage_user():
    while True:
        user_list = load_data_file("data/user.txt")
        try:
            choice = int(input("==== User Management ====\n1) view user data\n2) Change name\n3) Change password\n4) add user\n5)exit\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            for user in user_list:
                print(f"User ID = {user["user_id"]}, name = {user["name"]}, role = {user["role"]}, password = {user["password"]}")
        elif choice == 2:
            wrong_name = str(input("enter the name that you want to change: "))
            correct_name = str(input("enter the correct name: "))
            name_exists = any(user["name"] == wrong_name for user in user_list)
            if not name_exists:
                print("Please enter a valid input.")
                continue
            for user in user_list:
                if user["name"] == wrong_name:
                    user["name"] = correct_name
                    if user["role"] == "student":
                        change_data("data/student.txt","name",wrong_name,correct_name)
                        change_data("data/report.txt","name",wrong_name,correct_name)
                    elif user["role"] == "teacher":
                        change_data("data/course.txt","teacher",wrong_name,correct_name)
            save_data_file("data/user.txt", user_list)
        elif choice == 3:
            wrong_password = str(input("enter the password that you want to change: "))
            correct_password = str(input("enter the correct password: "))
            password_exists = any(user["password"] == wrong_password for user in user_list)
            if not password_exists:
                print("Please enter a valid input.")
                continue
            for user in user_list:
                if user["password"] == wrong_password:
                    user["password"] = correct_password
            save_data_file("data/user.txt",user_list)
        elif choice == 4:
            name = input("Enter name: ")
            password = input("Enter password: ")
            role = input("Enter role: ")
            if not name or not password:
                print("please enter a valid name or password")
            if role.lower() not in ["admin","teacher","student","staff"]:
                print("please enter a valid role")
                continue
            add_user(name, role, password)
        elif choice == 5:
            break
        else:
            print("please enter a valid number")

def resources_allocation():
    while True:
        user_list = load_data_file("data/user.txt")
        try:
            choice = int(input("==== resources allocation ====\n1) view resources\n2) update resources\n3)exit\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            view_resources()
        elif choice == 2:
            add_update_resource()
        elif choice == 3:
            break
        else:
            print("please enter a valid number")


def admin():
    while True:
        try:
            admin_input =int(input("==== Admin Manu ====\n1)manage user\n2)student management\n3)manage course\n4)manage schedule\n5)generate report\n6）allocate resources\n7)exit"))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if admin_input == 1:
            manage_user()
        elif admin_input == 2:
            student_management()
        elif admin_input == 3:
            course_management()
        elif admin_input == 4:
            schedule_management()
        elif admin_input == 5:
            generate_report()
        elif admin_input == 6:
            resources_allocation()
        elif admin_input == 7:
            break
        else:
            print("please enter a valid number")


def login():
    while True:
        try:
            user_input =int(input("==== login ====\n1) login\n2) create account(For student only) "))
        except ValueError:
            print("Enter a valid input!")
            continue
        if user_input == 1:
            user_role = str(input("admin/student/staff/teacher\nenter your role: "))
            user_password = str(input("Enter your password: "))
            data_list = load_data_file("data/user.txt")
            for user in data_list:
                if user_role.lower() == user["role"].lower() and user_password == user["password"]:
                    print(f"Welcome, {user['name']} ({user['role']})!")
                    if user["role"] == "student":
                        student_menu(user["name"])
                        return
                    elif user["role"] == "admin":
                        admin()
                        return
                    elif user["role"] == "staff":
                        staff()
                        return
                    elif user["role"] == "teacher":
                        teacher()
                        return
            print("Invalid role or password. Please try again.")
            break
        elif user_input == 2:
            name = str(input("Enter your name: "))
            password = str(input("Enter your password: "))
            age = int(input("Enter your age: "))
            add_student()
            add_user(name,"student",password)

login()