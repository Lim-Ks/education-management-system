import json
from sharedfunction import *
from teacher import *
def add_user(name, role, password):
    user_list = load_data_file("user.txt")
    for number, data in enumerate(user_list):
        if number == len(user_list)-1:
            new_user_id = data["user_id"]+1
    new_data = {"user_id": new_user_id, "name": name, "role": role, "password": password}
    user_list.append(new_data)
    write_file("user.txt",user_list)


def add_student(name,age):
    student_list =load_data_file("student.txt")
    for number, data in enumerate(student_list):
        if number == len(student_list)-1:
            student_id = data["student_id"]
    student_id_number = int(student_id.replace("S","")) +1
    new_student_id = f"S{student_id_number}"
    new_student = {"student_id":new_student_id, "student_name":name, "age": age, "course_id": []}
    student_list.append(new_student)
    write_file("student.txt",student_list)


def change_student(wrong_name,correct_name):
    student_list=load_data_file("student.txt")
    for student in student_list:
        if wrong_name == student["student_name"]:
            student["student_name"] = correct_name
    write_file("student.txt",student_list)


def change_report(wrong_name,correct_name):
    reports_list =load_data_file("report.txt")
    for report in reports_list:
        if wrong_name == report["name"]:
            report["name"] = correct_name
    write_file("report.txt",report_list)


def change_teacher(wrong_name,correct_name):
    teacher_list=load_data_file("course.txt")
    for teacher in teacher_list:
        if wrong_name == teacher["teacher"]:
            teacher["teacher"] = correct_name
    write_file("course.txt",teacher_list)


def manage_user():
    while True:
        user_list = load_data_file("user.txt")
        try:
            choice = int(input("==== User Management ====\n1)view user data\n2) Change name\n3) Change password\n4) exit\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        if choice == 1:
            read_file("user.txt")
        elif choice == 2:
            read_file("user.txt")
            wrong_name = str(input("enter the name that you want to change: "))
            correct_name = str(input("enter the correct name: "))
            for user in user_list:
                if user["name"] == wrong_name:
                    user["name"] = correct_name
                    if user["role"] == "student":
                        change_student(wrong_name, correct_name)
                        change_report(wrong_name, correct_name)
                    elif user["role"] == "teacher":
                        change_teacher(wrong_name, correct_name)
            rite_file("user.txt", user_list)
        elif choice == 3:
            read_file("user.txt")
            wrong_password = str(input("enter the password that you want to change: "))
            correct_password = str(input("enter the correct password: "))
            for user in user_list:
                if user["password"] == wrong_password:
                    user["password"] = correct_password
            write_file("user.txt",user_list)
        elif choice == 4:
            break
        else:
            print("please enter a valid number")


def admin():
    while True:
        try:
            admin_input =int(input("==== Admin Manu ====\n1)manage user\n2)view student profile\n3)manage course\n4)manage schedule\n5)generate report\n6)exit"))
        except ValueError:
            print("Invalid input. Please enter a number")
        if admin_input == 1:
            manage_user()
        elif admin_input == 2:
            read_file("student.txt")
        elif admin_input == 3:
            course_management()
        elif admin_input == 4:
            schedule_management()
        elif admin_input == 5:
            generate_report()
        elif admin_input == 6:
            break
        else:
            print("please enter a valid number")


def login():
    while True:
        user_input =int(input("==== login ====\n1) login\n2) create account(For student only) "))
        if user_input == 1:
            user_role = str(input("admin/student/staff/teacher\nenter your role: "))
            user_password = str(input("Enter your password: "))
            data_list = load_data_file("user.txt")
            for user in data_list:
                if user_role.lower() == user["role"].lower() and user_password == user["password"]:
                    print(f"Welcome, {user['name']} ({user['role']})!")
                    if user["role"] == "student":
                        student(user["name"])
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
            add_student(name, age)
            add_user(name,"student",password)

