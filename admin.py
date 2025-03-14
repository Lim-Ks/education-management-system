from sharedfunction import *
from teacher import *
from student import *
from staff import *


def change_data(file_name,data_key,wrong_data,correct_data):
    data_list =load_data_file(file_name)
    for data in data_list:
        if wrong_data == data[data_key]:
            data[data_key] = correct_data
    save_data_file(file_name,data_list)


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
            if correct_name:
                for user in user_list:
                    if user["name"] == wrong_name:
                        user["name"] = correct_name
                        if user["role"] == "student":
                            change_data("data/student.txt","name",wrong_name,correct_name)
                            change_data("data/report.txt","name",wrong_name,correct_name)
                        elif user["role"] == "teacher":
                            change_data("data/course.txt","teacher",wrong_name,correct_name)
                save_data_file("data/user.txt", user_list)
            else:
                print("name cannot be blank")
        elif choice == 3:
            wrong_password = str(input("enter the password that you want to change: "))
            correct_password = str(input("enter the correct password: "))
            password_exists = any(user["password"] == wrong_password for user in user_list)
            if not password_exists:
                print("Please enter a valid input.")
                continue
            if correct_password:
                for user in user_list:
                    if user["password"] == wrong_password:
                        user["password"] = correct_password
                save_data_file("data/user.txt",user_list)
            else:
                print("password cannot be blank")
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


def schedule_management():
    while True:
        schedule_list =load_data_file("data/schedule.txt")
        course_list =load_data_file("data/course.txt")
        try:
            user_input = int(input("==== Schedule Management ====\n1)view schedule\n2)change data\n3)exit\nEnter a number: "))
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
                    if wrong_key not in ["course_id","date","time","location"]:
                        print("Invalid Key")
                        continue
                    correct_value = str(input("Enter the correct data: "))
                    if wrong_key == "course_id":
                        exists = any(course["course_id"] == correct_value for course in course_list)
                        if not exists:
                            print("Please enter a valid course id.")
                            continue
                    if correct_value:
                        schedule[wrong_key] = correct_value
                        save_data_file("data/schedule.txt",schedule_list)
                        print("update successfully")
                    else:
                        print("correct data cannot be empty")
            if found == False:
                print("Schedule not found")
                continue
        elif user_input == 3:
            break
        else:
            print("please enter a valid number")


def student_management():
    while True:
        student_list = load_data_file("data/student.txt")
        grade_list = load_data_file("data/grade.txt")
        try:
            choice = int(input("==== Student Management ====\n1)view student\n2)update student profile\n3)view student grade\n4)exit\nEnter your choice: "))
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
            student_id = input("Enter the student id: ")
            found = False
            for student in student_list:
                if student["student_id"] == student_id:
                    found = True
                    wrong_key = input("age, phone_num, emergency_num, enrollment_status, status\nenter the data key that you want to change: ")
                    if wrong_key not in ["age","phone_num","emergency_num","enrollment_status","status"]:
                        print("Invalid key")
                        continue
                    correct_value = input("enter the correct data: ")
                    if correct_value:
                        student[wrong_key] = correct_value
                        save_data_file("data/student.txt",student_list)
                        print("update successfully")
                    else:
                        print("correct data cannot be empty")
            if found == False:
                print("student not found")
                continue
        elif choice == 3:
            for grade in grade_list:
                print("------------")
                print("student id: ", grade["student_id"])
                print("name: ", grade["course_id"])
                print("exam score: ", grade["exam_score"])
                print("exam grade: ", grade["exam_grade"])
                print("assignment score: ", grade["assignment_score"])
                print("assignment grade: ", grade["assignment_grade"])
                print("teacher feedback: ", grade["feedback"])
                print("------------")
        elif choice == 4:
            break


def generate_report():
    while True:
        report_list = load_data_file("data/report.txt")
        grade_list = load_data_file("data/grade.txt")
        student_list = load_data_file("data/student.txt")
        attendance_list = load_data_file("data/attendance.txt")
        course_list = load_data_file("data/course.txt")
        financial_list = load_data_file("data/financial report.txt")
        try:
            admin_input = int(input("===== Report Generation =====\n1)view report\n2)update report / financial report\n3)generate report\n4)generate financial report\n5)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if admin_input == 1:
            try:
                choice = int(input("1)report\n2)financial report\nchoose the report that you want to view: "))
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
                    print("total fee: ", finance["total_fee"])
                    print("total paid: ", finance["total_paid"])
                    print("outstanding: ",finance["outstanding"])
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
                        wrong_key = str(input("course, grade, attendance, teacher review\nEnter the data type that need to update: "))
                        if wrong_key not in ["course","grade","attendance","teacher review"]:
                            print("Please enter a valid input")
                            continue
                        if correct_value:
                            correct_value = str(input("Enter the correct data"))
                            change_report[wrong_key] =correct_value
                            save_data_file("data/report.txt", report_list)
                            print("update successfully")
                if found == False:
                    print(f"{student_id} report not found")
            elif choice == 2:
                for finance in financial_list:
                    if student_id ==finance["student_id"]:
                        found = True
                        change_financial_report = finance
                        wrong_key = str(input("total fee, total paid, outstanding\nEnter the data type that need to update: "))
                        if wrong_key not in ["total fee","total paid","outstanding"]:
                            print("Please enter a valid input")
                            continue
                        correct_value = str(input("Enter the correct data"))
                        if correct_value:
                            change_financial_report[wrong_key] =correct_value
                            save_data_file("data/financial report.txt", financial_list)
                        else:
                            print("correct data cannot be empty")
                if found == False:
                    print(f"{student_id} report not found")
        elif admin_input == 3:
            student_id = str(input("Enter the student id: "))
            course_id =str(input("Enter the course id: "))
            teacher_review = str(input("Enter the teacher review(or press Enter to leave it blank): "))
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
            financial_list.append(new_financial_report)
            save_data_file("data/financial report.txt",financial_list)
            print("create successfully")
        elif admin_input == 5:
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
            add_student()

