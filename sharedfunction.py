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

def change_data(file_name,data_key,wrong_data,correct_data):
    data_list =load_data_file(file_name)
    for data in data_list:
        if wrong_data == data[data_key]:
            data[data_key] = correct_data
    save_data_file(file_name,data_list)



def add_user(name, role, password):
    user_list = load_data_file("data/user.txt")
    for number, data in enumerate(user_list):
        if number == len(user_list)-1:
            new_user_id = data["user_id"]+1
    new_data = {"user_id": new_user_id, "name": name, "role": role, "password": password}
    user_list.append(new_data)
    save_data_file("data/user.txt",user_list)


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
                        course_name = course["course_name"]
                print("------------")
                print("course name: ", schedule["course_name"])
                print("date: ", schedule["date"])
                print("duration: ", schedule["time"])
                print("location: ", schedule["location"])
                print("------------")
        elif user_input == 2:
            try:
                wrong_key = str(input("date, time, location\nEnter the data name: "))
                wrong_value = str(input("Enter the wrong data: "))
                correct_value = str(input("Enter the correct data: "))
                exists = any(schedule[wrong_key] == wrong_value for schedule in schedule_list)
                if not exists:
                    print("Please enter a valid input.")
                    continue
            except KeyError:
                print("Please enter a valid input ")
                continue
            if correct_value:
                change_data("data/schedule.txt", wrong_key, wrong_value, correct_value)
            else:
                print("correct data cannot be blank!")
                continue
            print("update successfully")
        elif user_input == 3:
            break
        else:
            print("please enter a valid number")


def course_management():
    while True:
        course_list =load_data_file("data/course.txt")
        user_list = load_data_file("data/user.txt")
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
            if not course_name or not teacher:
                print("course name or teacher cannot be blank")
            create = False
            for user in user_list:
                if user["role"] == "teacher:":
                    if user["name"] == teacher:
                        create = True
            if create == True:
                new_course = {"course_id":new_course_id,"course_name":course_name,"teacher":teacher}
                course_list.append(new_course)
                save_data_file("data/course.txt", course_list)
                print("create successfully")
            else:
                print("teacher not found")
        elif admin_input == 2:
            try:
                wrong_key = str(input("course_id / course_name / teacher\nEnter the things that you want to change: "))
                wrong_value = str(input("Enter the wrong data: "))
                correct_value = str(input("Enter the correct one: "))
                exists = any(course[wrong_key] == wrong_value for course in course_list)
                if not exists:
                    print("Please enter a valid input.")
                    continue
                if correct_value:
                    change_data("data/course.txt", wrong_key, wrong_value, correct_value)
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
            save_data_file("data/course.txt",course_list)
            print("Delete successfully")
        elif admin_input == 4:
            for course in course_list:
                print(f"course id = {course["course_id"]}, course name = {course["course_name"]}, teacher = {course["teacher"]}")
        elif admin_input == 5:
            break
        else:
            print("please enter a valid number")

