import json

from sharedfunction import *
# File paths
Course_File = "course.txt"
Student_File = "student.txt"
Grade_File = "grade.txt"
Attendance_File = "attendance.txt"
Report_File = "report.txt"

def load_data_file(file_name):
    with open (file_name,"r")as file:
        all_data = json.load(file)
    return all_data


def write_file(file_name,data):
    with open(file_name,"w") as file:
        file.write("[\n")
        for number, person in enumerate(data):
            file.write(f'  {json.dumps(person)}')
            if number < len(data) - 1:
                file.write(",\n")
        file.write("\n]")
# course creation
def add_new_course():
    data = load_data_file(Course_File)
    course_id = str(input("Enter the course id:"))
    course_name =  str(input("Enter the course name:"))
    lecturer = str(input("Enter lecturer name:"))
    schedules = str(input("Enter schedules(e.g., Mon 8AM - 10AM):"))
    lesson_plan = str(input("Enter lesson plan:"))
    assignment = str(input("Enter assignment:"))

    # check if course already exists
    if course_id in Course_File:
        print(f"{course_id},{course_name} is already exists in Course File.")
        return
    # add new course
    else:
        new_course = {"Course ID": course_id,"Course Name": course_name, "Lecturer": lecturer, "Schedules": schedules,
                                "Lesson Plan": lesson_plan,"Assignment": assignment}
        data.append(new_course)
        write_file(Course_File,data)
        print(f"Course {course_id},{course_name} created successfully!")


# course management
def update_course():
    data = load_data_file(Course_File)
    course_id = str(input("Enter the course id:")).strip()

    for courses in data:
        # check if course exists
        if course_id == courses["Course ID"]:
            print(f"Current course:{courses["Course Name"]}")
            print(f"Current lecturer:{courses["Lecturer"]}")
            print(f"Current schedules:{courses["Schedules"]}")
            print(f"Current lesson plan:{courses["Lesson Plan"]}")
            print(f"Current assignment:{courses["Assignment"]}")
        # enter new information
            new_course_name = str(input("Enter new course name(or press enter to keep current)"))
            new_lecturer = str(input("Enter new lecturer(or press enter to keep current):"))
            new_schedules = str(input("Enter new schedules(or press enter to keep current):"))
            new_lesson_plan = str(input("Enter new lesson plan(or press enter to keep current):"))
            new_assignment = str(input("Enter new assignment(or press enter to keep current):"))

            courses["Course Name"] = new_course_name
            courses["Lecturer"] = new_lecturer
            courses["Schedules"] = new_schedules
            courses["Lesson Plan"] = new_lesson_plan
            courses["Assignment"] = new_assignment

            write_file(Course_File,data)
            print(f"{course_id} has been updated successfully!")
            return
        else:
            print(f"Course {course_id} not found.")

def enroll_student():
    data = load_data_file(Student_File)
    course_id = str(input("Enter course id:"))
    student_id = str(input("Enter student id:"))
    student_name = str(input("Enter student name:"))
    for student in data:
        if student["student_id"] == student_id:
            for course in student["course_id"]:
                if course == course_id:
                    print(f"Student {student_id},{student_name} is already enrolled in course {course_id}.")
                    return
                else:
                    student["course_id"].append(course_id)
                    write_file(Student_File, data)
                    print(f"Student {student_id},{student_name} is successfully enroll in course {course_id}.")
                    return

    print(f"Student {student_id},{student_name} not found.")

#remove student course
def remove_student():
    data = load_data_file(Student_File)
    student_id = str(input("Enter the student id:"))
    course_id = str(input("Enter course id:"))

    for student in data:
        if student["student_id"] == student_id:
            for course in student["course_id"]:
                if course == course_id:
                    student["course_id"].remove(course_id)
                    write_file(Student_File,data)
                    print(f"Course {course_id} is removed from student {student_id}.")
                    return
                else:
                    print(f"Course {course_id} not found.")

    print(f"Student {student_id} not found.")

def grade():
    data = load_data_file(Grade_File)
    student_id = str(input("Enter student id:"))
    exam_score = int(input("Enter exam score:"))
    asg_score = int(input("Enter assignment score:"))
    feedback = str(input("Enter feedback:"))

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

    for student in data:
        if student_id == student["student_id"]:
            print(f"Student {student_id} already exists.")
            return

    new_student = {"student_id": student_id, "exam_score": exam_score, "exam_grade": exam_grade,
                   "assignment_score": asg_score,"assignment_grade": asg_grade,"feedback": feedback}
    data.append(new_student)
    write_file(Grade_File, data)
    print(f"Student {student_id} added.")
    print(f"Student {student_id} exam_score: {exam_score}")
    print(f"Student {student_id} exam_grade: {exam_grade}")
    print(f"Student {student_id} assignment_score: {asg_score}")
    print(f"Student {student_id} assignment_grade: {asg_grade}")
    print(f"Feedback:{feedback}")

def attendance_tracking():
    data = load_data_file(Attendance_File)
    student_id = str(input("Enter student id:"))
    course_id = str(input("Enter course id:"))
    attendance_date = str(input("Enter date:"))

    valid_status = ["absent","present"]
    status = str(input("Enter attendance status(absent/present):"))

    if status.lower() not in valid_status:
        print("Invalid status. Please enter 'present' or 'absent'.")
        status = str(input("Enter attendance status(Absent/Present):"))

    for record in data:
        if record["student_id"] == student_id and record["course_id"] == course_id and record["date"] == attendance_date:
            print(f"Attendance record for student {student_id} on {attendance_date} is already exists.")
            return

    new_record = {"student_id": student_id,"course_id": course_id,"date": attendance_date,"status": status.lower()}
    data.append(new_record)
    write_file(Attendance_File,data)
    print(f"Attendance recorded: {student_id} was {status} on {attendance_date}.")

def calculate_attendance(student_id,data):

    total_days = 0
    present_days = 0

    for record in data:
        if record["student_id"] == student_id:
            total_days += 1
            if record["status"].lower() == 'present':
                present_days += 1

    if total_days == 0:
        return None

    percentage = (present_days/total_days) * 100
    return percentage

def teacher():
    while True:
        print("\n===== Teacher Management System =====")
        print("1. Course Creation and Management")
        print("2. Student Enrollment")
        print("3. Grading and Assessment")
        print("4. Attendance Tracking")
        print("5. Report Generation")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            print("===== Course Creation and Management =====")
            print("1. Add New Course")
            print("2. Update Course")
            print("3. Manage Schedule")

            try:
                course = int(input("Enter your choice (1-3): "))
            except ValueError:
                print("Invalid input. Please enter 1, 2 or 3.")
                continue

            if course == 1:
                add_new_course()
            elif course == 2:
                update_course()
            elif course == 3:
                course_management()
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
            generate_report()

        elif choice == 6:
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

