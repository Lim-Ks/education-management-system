import json

def load_data_file(file_name):
    with open (file_name,"r")as file:
        all_data = json.load(file)
    return all_data


def save_data_file(file_name,data):
    with open(file_name,"w") as file:
        file.write("[\n")
        for number, person in enumerate(data):
            file.write(f'  {json.dumps(person)}')
            if number < len(data) - 1:
                file.write(",\n")
        file.write("\n]")


def read_file(file_name):
    with open (file_name,"r") as file:
        all_data = json.load(file)
        for data in all_data:
            print(data)


def change_data(file_name,data_key,wrong_data,correct_data):
    data_list =load_data_file(file_name)
    for data in data_list:
        if wrong_data == data[data_key]:
            data[data_key] = correct_data
    save_data_file(file_name,data_list)


def schedule_management():
    while True:
        schedule_list =load_data_file("schedule.txt")
        course_list =load_data_file("course.txt")
        try:
            user_input = int(input("==== Schedule Management ====\n1)view schedule\n2)change data\n3)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if user_input == 1:
            for schedule in schedule_list:
                for course in course_list:
                    if course["course_id"] == schedule["course_id"]:
                        course_name = course["course_name"]
                print("------------")
                print("course name: ", course_name)
                print("date: ", schedule["date"])
                print("duration: ", schedule["time"])
                print("location: ", schedule["location"])
                print("------------")
        elif user_input == 2:
            try:
                wrong_key = str(input("data, time, location\nEnter the data name: "))
                wrong_value = str(input("Enter the wrong data: "))
                correct_value = str(input("Enter the correct data: "))
                change_data("schedule.txt",wrong_key,wrong_value, correct_value)
                exists = any(schedule[wrong_key] == wrong_value for schedule in schedule_list)
                if not exists:
                    print("Please enter a valid input.")
                    continue
            except KeyError:
                print("Please enter a valid input ")
                continue
        elif user_input == 3:
            break
        else:
            print("please enter a valid number")


def course_management():
    while True:
        course_list =load_data_file("course.txt")
        try:
            admin_input = int(input("==== Course Management ====\n1)create course\n2)update course\n3)delete course\n4)view course\n5)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if admin_input == 1:
            for number, data in enumerate(course_list):
                if number == len(course_list) - 1:
                    course_id = data["course_id"]
            course_id_number = int(course_id.replace("CS", "")) + 1
            new_course_id = f"CS{course_id_number}"
            course_name = str(input("Enter the course name: "))
            teacher = str(input("Enter the teacher name: "))
            new_course = {"course_id":new_course_id,"course_name":course_name,"teacher":teacher}
            course_list.append(new_course)
            save_data_file("course.txt", course_list)
        elif admin_input == 2:
            try:
                wrong_key = str(input("course_id / course_name / teacher\nEnter the things that you want to change: "))
                wrong_value = str(input("Enter the wrong data: "))
                correct_value = str(input("Enter the correct one: "))
                change_data("course.txt",wrong_key,wrong_value,correct_value)
                exists = any(course[wrong_key] == wrong_value for course in course_list)
                if not exists:
                    print("Please enter a valid input.")
                    continue
            except KeyError:
                print("Please enter a valid input")
        elif admin_input == 3:
            delete_course = str(input("Enter the course_id that you want to delete: "))
            exists = any(course["course_id"] == delete_course for course in course_list)
            if not exists:
                print("Please enter a valid input.")
                continue
            for course in course_list:
                if course["course_id"] == delete_course:
                    course_list.remove(course)
            save_data_file("course.txt",course_list)
            print("Delete successfully")
        elif admin_input == 4:
            read_file("course.txt")
        elif admin_input == 5:
            break
        else:
            print("please enter a valid number")


def generate_report():
    while True:
        report_list = load_data_file("report.txt")
        grade_list = load_data_file("grade.txt")
        student_list = load_data_file("student.txt")
        attendance_list = load_data_file("attendance.txt")
        course_list = load_data_file("course.txt")
        try:
            admin_input = int(input("===== Report Generation =====\n1)view report\n2)update report\n3)add report\n4)exit\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        with open("report.txt", "r") as file:
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
            for report in report_list:
                if student_id == report["student_id"]:
                    change_student = report
                    wrong_key = str(input("student id, name, course, grade, attendance, teacher review\nEnter the data type that need to update: "))
                    correct_value = str(input("Enter the correct data"))
                    change_student[wrong_key] =correct_value
            save_data_file("report.txt",report_list)
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
            save_data_file("report.txt",report_list)
        elif admin_input == 4:
            break
        else:
            print("please enter a valid number")
