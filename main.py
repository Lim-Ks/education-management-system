import json

def student(name):
    student_name =name
    with open("student.txt","r") as students:
        student_detail = json.load(students)
        for student in student_detail:
            if student_name == student["student_name"]:
                student_data = student
                print(student_data)
    while True:
        student_input =int(input("Enter your choice:\n1)check my course\n2)check the schedule\n3)watch my report\n4)exit"))
        if student_input == 1:
            with open("course.txt", "r") as file:
                data = json.load(file)
                for course in data:
                    if student_data["Course_id"] == course ["course_id"]:
                        print("------------")
                        print("Course ID:", course["course_id"])
                        print("Course name:", course["course_name"])
                        print("Teacher:", course["teacher"])
                        print("------------")
        elif student_input == 2:
            with open ("schedule.txt","r") as file:
                schedules = json.load(file)
                for schedule in schedules:
                    if student_data["course_id"] == schedule ["course_id"]:
                        print("------------")
                        print("Date:", schedule["date"])
                        print("Time:", schedule["time"])
                        print("Location:",schedule["location"])
                        print("------------")
        elif student_input == 3:
            with open ("report.txt","r")as file:
                reports = json.load(file)
                for report in reports:
                    if student_data["student_id"] == report["student_id"]:
                        print("------------")
                        print("Name:", report["name"])
                        print("Course:", report["course"])
                        print("Grade:", report["grade"])
                        print("Attendance:", report["attendance"])
                        print("------------")
        elif student_input == 4:
            break


def add_user(user_id, name, role, password):
    with open("user.txt", "r") as file:
        existing_data = json.load(file)

    new_data = {"user_id": user_id, "name": name, "role": role, "password": password}
    existing_data.append(new_data)

    with open("user.txt", "w") as file:
        file.write("[\n")
        for i, person in enumerate(existing_data):
            file.write(f'  {json.dumps(person)}')
            if i < len(existing_data) - 1:
                file.write(",\n")
        file.write("\n]")
    print("Data saved successfully!")


def read_user():
    with open("user.txt", "r") as file:
        users = json.load(file)
        for user in users:
            print(user)


def read_student():
    with open("student.txt", "r") as file:
        students = json.load(file)
        for student in students:
            print(student)


def change_student(wrong_name,correct_name):
    student_list=[]
    with open("student.txt","r") as file:
        students = json.load(file)
        for student in students:
            if wrong_name != student["student_name"]:
                student_list.append(student)
            elif wrong_name == student["student_name"]:
                student["student_name"] = correct_name
                student_list.append(student)

    with open("student.txt","w") as new_data:
        new_data.write("[\n")
        for student, person in enumerate(student_list):
            new_data.write(f'  {json.dumps(person)}')
            if student < len(student_list) - 1:
                new_data.write(",\n")
        new_data.write("\n]")


def change_report(wrong_name,correct_name):
    report_list=[]
    with open("report.txt","r") as file:
        reports = json.load(file)
        for report in reports:
            if wrong_name != report["name"]:
                report_list.append(report)
            elif wrong_name == report["name"]:
                report["name"] = correct_name
                report_list.append(report)

    with open("report.txt","w") as new_data:
        new_data.write("[\n")
        for report, person in enumerate(report_list):
            new_data.write(f'  {json.dumps(person)}')
            if report < len(report_list) - 1:
                new_data.write(",\n")
        new_data.write("\n]")


def change_teacher(wrong_name,correct_name):
    teacher_list=[]
    with open("course.txt","r") as file:
        teachers = json.load(file)
        for teacher in teachers:
            if wrong_name != teacher["teacher"]:
                teacher_list.append(teacher)
            elif wrong_name == teacher["teacher"]:
                teacher["teacher"] = correct_name
                teacher_list.append(teacher)

    with open("course.txt","w") as new_data:
        new_data.write("[\n")
        for teacher, person in enumerate(teacher_list):
            new_data.write(f'  {json.dumps(person)}')
            if teacher < len(teacher_list) - 1:
                new_data.write(",\n")
        new_data.write("\n]")


def change_data():
    user_list = []
    try:
        choice = int(input("1) Change name\n2) Change password\nEnter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if choice == 1:
        read_user()
        wrong_name = str(input("enter the name that you want to change: "))
        correct_name = str(input("enter the correct name: "))
        with open ("user.txt","r") as file:
            users = json.load(file)
            for user in users:
                if user["name"] !=wrong_name:
                    user_list.append(user)
                else:
                    wrong_data =user
                    user["name"] = correct_name
                    user_list.append(user)
                    if user["role"] == "student":
                        change_student(wrong_name,correct_name)
                        change_report(wrong_name,correct_name)
                    elif user["role"] == "teacher":
                        change_teacher(wrong_name,correct_name)
        with open ("user.txt","w") as new:
            new.write("[\n")
            for user, person in enumerate(user_list):
                new.write(f'  {json.dumps(person)}')
                if user < len(user_list) - 1:
                    new.write(",\n")
            new.write("\n]")
    elif choice == 2:
        read_user()
        wrong_password = str(input("enter the password that you want to change: "))
        correct_password = str(input("enter the correct password: "))
        with open("user.txt", "r") as file:
            users = json.load(file)
            for user in users:
                if user["password"] != wrong_password:
                    user_list.append(user)
                else:
                    wrong_data = user
                    user["password"] = correct_password
                    user_list.append(user)
    with open("user.txt", "w") as new_data:
        new_data.write("[\n")
        for user, person in enumerate(user_list):
            new_data.write(f'  {json.dumps(person)}')
            if user < len(user_list) - 1:
                new_data.write(",\n")
        new_data.write("\n]")


def course_management():
    course_list =[]
    admin_input = int(input("1)create course\n2)update course\n3)delete course\nEnter a number: "))
    if admin_input == 1:
        course_id = str(input("Enter the new course_id: "))
        course_name = str(input("Enter the course name: "))
        teacher = str(input("Enter the teacher name: "))
        new_course = {"course_id":course_id,"course_name":course_name,"teacher":teacher}
        with open("course.txt", "r") as file:
            courses = json.load(file)
            for course in courses:
                course_list.append(course)
        course_list.append(new_course)
        with open ("course.txt","w") as file:
            file.write("[\n")
            for course, subject in enumerate(course_list):
                file.write(f'  {json.dumps(subject)}')
                if course < len(course_list) - 1:
                    file.write(",\n")
            file.write("\n]")
    elif admin_input == 2:
        wrong = str(input("Enter the things that you want to change: \ncourse_id\ncourse_name\nteacher"))
        wrong_key = str(input("Enter the wrong data: "))
        correct_key = str(input("Enter the correct one: "))
        with open("course.txt","r") as file:
            courses = json.load(file)
            for course in courses:
                if course[wrong] != wrong_key:
                    course_list.append(course)
                else:
                    course[wrong] = correct_key
                    course_list.append(course)
        with open ("course.txt","w") as file:
            file.write("[\n")
            for course, subject in enumerate(course_list):
                file.write(f'  {json.dumps(subject)}')
                if course < len(course_list) - 1:
                    file.write(",\n")
            file.write("\n]")
    elif admin_input == 3:
        delete_course = str(input("Enter the course_id that you want to delete: "))
        with open("course.txt","r") as file:
            courses = json.load(file)
            for course in courses:
                if course["course_id"] != delete_course:
                    course_list.append(course)
        with open ("course.txt","w") as file:
            file.write("[\n")
            for course, subject in enumerate(course_list):
                file.write(f'  {json.dumps(subject)}')
                if course < len(course_list) - 1:
                    file.write(",\n")
            file.write("\n]")


def admin():
    while True:
        admin_input =int(input("1)view user data\n2)view student profile\n3)change user data\n4)manage course"))
        if admin_input == 1:
            read_user()
        elif admin_input == 2:
            read_student()
        elif admin_input == 3:
            change_data()
        elif admin_input == 4:
            course_management()


def login():
    while True:
        user_role = str(input("enter your role: "))
        user_password = str(input("Enter your password: "))
        with open("user.txt") as file:
            data = json.load(file)
            for user in data:
                if user_role.lower() == user["role"].lower() and user_password == user["password"]:
                    print(f"Welcome, {user['name']} ({user['role']})!")
                    if user["role"] == "student":
                        student(user["name"])
                        return
                    elif user["role"] == "admin":
                        admin()
                    elif user["role"] == "staff":
                        staff()
                    elif user["role"] == "teacher":
                        teacher()
            print("Invalid role or password. Please try again.")
            break
