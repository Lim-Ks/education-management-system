from sharedfunction import *
from teacher import *
from student import *
from staff import *

def add_user(name, role, password):
    user_list = load_data_file("user.txt")
    for number, data in enumerate(user_list):
        if number == len(user_list)-1:
            new_user_id = data["user_id"]+1
    new_data = {"user_id": new_user_id, "name": name, "role": role, "password": password}
    user_list.append(new_data)
    save_data_file("user.txt",user_list)


def student_management():
    while True:
        student_list = load_data_file("student.txt")
        grade_list = load_data_file("grade.txt")
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
                change_data("student.txt", wrong_key, wrong_value, correct_value)
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
        user_list = load_data_file("user.txt")
        try:
            choice = int(input("==== User Management ====\n1) view user data\n2) Change name\n3) Change password\n4) exit\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            read_file("user.txt")
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
                        change_data("student.txt","name",wrong_name,correct_name)
                        change_data("report.txt","name",wrong_name,correct_name)
                    elif user["role"] == "teacher":
                        change_data("course.txt","teacher",wrong_name,correct_name)
            save_data_file("user.txt", user_list)
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
            save_data_file("user.txt",user_list)
        elif choice == 4:
            break
        else:
            print("please enter a valid number")


def admin():
    while True:
        try:
            admin_input =int(input("==== Admin Manu ====\n1)manage user\n2)student management\n3)manage course\n4)manage schedule\n5)generate report\n6)exit"))
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
            data_list = load_data_file("user.txt")
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