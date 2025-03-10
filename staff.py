import re
from datetime import datetime
from sharedfunction import *
from student import add_student
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_student_id(student_id):
    pattern = r'^S\d{3}$'
    return re.match(pattern, student_id)

def validate_resource_id(resource_id):
    pattern = r'^R\d{3}$'
    return re.match(pattern, resource_id)

#main menu####
def staff():
    while True:
        print("\nStaff Management System")
        print("1. Manage Student Records")
        print("2. Timetable Management")
        print("3. Resource Allocation")
        print("4. Event Management")
        print("5. Communication")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manage_student_records()
        elif choice == "2":
            manage_timetable()
        elif choice == "3":
            manage_resources()
        elif choice == "4":
            manage_events()
        elif choice == "5":
            manage_communication()
        elif choice == "6":
            print("Exiting Staff Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

#student records

def manage_student_records():
    while True:
        print("\nStudent Records Management")
        print("1. Register Student")
        print("2. Transfer Student")
        print("3. Withdraw Student")
        print("4. View Student Records")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            transfer_student()
        elif choice == "3":
            withdraw_student()
        elif choice == "4":
            view_student_records()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def transfer_student():
    print("\nTransfer Student")
    student_id = input("Enter Student ID to transfer: ").strip()
    if not validate_student_id(student_id):
        print("Invalid Student ID format. It must be in the format S followed by 6 digits (e.g., S000).")
        return
    records = load_data_file("data/student.txt")
    found = False
    for record in records:
        if record("student_id") == student_id:
            new_name = input("Enter new name (or press Enter to keep unchanged): ").strip()
            if new_name:
                record["name"] = new_name.title()
            record["status"] = "transferred"
            found = True
    if found:
        save_data_file("data/student.txt", records)
        print("Student transferred successfully.")
    else:
        print("Student not found.")

def withdraw_student():
    print("\nWithdraw Student")
    student_id = input("Enter Student ID to withdraw: ").strip()
    if not validate_student_id(student_id):
        print("Invalid Student ID format. It must be in the format S followed by 3 digits (e.g., S000).")
        return
    records = load_data_file("data/student.txt")
    found = False
    for record in records:
        if record.get("student_id") == student_id:
            record["status"] = "withdrawn"
            found = True
    if found:
        save_data_file("data/student.txt", records)
        print("Student withdrawn successfully.")
    else:
        print("Student not found.")

def view_student_records():
    print("\nStudent Records:")
    records = load_data_file("data/student.txt")
    if not records:
        print("No student records found.")
    else:
        for record in records:
            print(record)
#timetable

def manage_timetable():
    while True:
        print("\nTimetable Management")
        print("1. Add Class Schedule")
        print("2. Update Class Schedule")
        print("3. Remove Class Schedule")
        print("4. View Class Schedule")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_schedule()
        elif choice == "2":
            update_schedule()
        elif choice == "3":
            remove_schedule()
        elif choice == "4":
            view_schedule()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_schedule():
    records = load_data_file("data/schedule.txt")
    title = input("Enter Schedule Title: ").strip()
    date = input("Enter Date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    time_val = input("Enter Time/Duration: ").strip()
    location = input("Enter Location: ").strip()
    new_record = {"title": title, "date": date, "time": time_val, "location": location}
    records.append(new_record)
    save_data_file("data/schedule.txt", records)
    print("Schedule added successfully.")

def update_schedule():
    records = load_data_file("data/schedule.txt")
    title = input("Enter Schedule Title to update: ").strip()
    found = False
    for record in records:
        if record.get("title").lower() == title.lower():
            print("\nCurrent schedule details:")
            print("Date:", record.get("date"))
            print("Time:", record.get("time"))
            print("Location:", record.get("location"))
            new_date = input("Enter new Date (YYYY-MM-DD) or press Enter to keep unchanged: ").strip()
            if new_date:
                if not validate_date(new_date):
                    print("Invalid date format. Skipping date update for this record.")
                else:
                    record["date"] = new_date
            new_time = input("Enter new Time or press Enter to keep unchanged: ").strip()
            if new_time:
                record["time"] = new_time
            new_location = input("Enter new Location or press Enter to keep unchanged: ").strip()
            if new_location:
                record["location"] = new_location
            found = True
    if found:
        save_data_file("data/schedule.txt", records)
        print("Schedule updated successfully.")
    else:
        print("No schedule found for the given title.")

def remove_schedule():
    records = load_data_file("data/schedule.txt")
    title = input("Enter Schedule Title to remove: ").strip()
    new_records = [record for record in records if record.get("title").lower() != title.lower()]
    if len(new_records) == len(records):
        print("No schedule found for that title.")
    else:
        save_data_file("data/schedule.txt", new_records)
        print("Schedule removed successfully.")

def view_schedule():
    records = load_data_file("data/schedule.txt")
    if not records:
        print("No schedule records found.")
    else:
        for record in records:
            print("------------")
            print("Title:", record.get("title"))
            print("Date:", record.get("date"))
            print("Time:", record.get("time"))
            print("Location:", record.get("location"))
            print("------------")

#resources
def manage_resources():
    while True:
        print("\nResource Allocation Management")
        print("1. Add/Update Resource")
        print("2. View Resources")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_update_resource()
        elif choice == "2":
            view_resources()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def add_update_resource():
    print("\nAdd or Update Resource Allocation")
    resource_id = input("Enter Resource ID (Format: R000): ").strip()
    if not resource_id:
        print("Resource ID cannot be empty.")
        return
    if not validate_resource_id(resource_id):
        print("Invalid Resource ID format.")
        return
    resource_name = input("Enter Resource Name: ").strip()
    if not resource_name:
        print("Resource Name cannot be empty.")
        return
    quantity_input = input("Enter Quantity: ").strip()
    try:
        quantity = int(quantity_input)
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Quantity must be a valid integer.")
        return
    allocated_to = input("Enter Allocated Class (or leave blank if not allocated): ").strip()
    record = {"resource_id": resource_id, "resource_name": resource_name, "quantity": quantity,
              "allocated_to": allocated_to}
    records = load_data_file("data/resources.txt")
    found = False
    for i, rec in enumerate(records):
        if rec.get("resource_id") == resource_id:
            records[i] = record
            found = True
            break
    if not found:
        records.append(record)
    save_data_file("data/resources.txt", records)
    print("Resource updated successfully.")


def view_resources():
    print("\nResources:")
    records = load_data_file("data/resources.txt")
    if not records:
        print("No resource records found.")
    else:
        for record in records:
            print(record)

#events

def manage_events():
    while True:
        print("\nEvent Management")
        print("1. Add Event")
        print("2. Update Event")
        print("3. Remove Event")
        print("4. View Events")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_event()
        elif choice == "2":
            update_event()
        elif choice == "3":
            remove_event()
        elif choice == "4":
            view_events()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_event():
    print("\nAdd Event")
    event_id = input("Enter Event ID: ").strip()
    if not event_id:
        print("Event ID cannot be empty.")
        return
    event_name = input("Enter Event Name: ").strip()
    if not event_name:
        print("Event Name cannot be empty.")
        return
    event_date = input("Enter Event Date (Format: YYYY-MM-DD): ").strip()
    if not validate_date(event_date):
        print("Invalid date format.")
        return
    event_description = input("Enter Event Description (leave blank if none): ").strip()
    record = {"event_id": event_id, "event_name": event_name, "event_date": event_date,
              "event_description": event_description}
    records = load_data_file("data/events.txt")
    records.append(record)
    save_data_file("data/events.txt", records)
    print("Event added successfully.")


def update_event():
    print("\nUpdate Event")
    event_id = input("Enter Event ID to update: ").strip()
    records = load_data_file("data/events.txt")
    updated = False
    for record in records:
        if record.get("event_id") == event_id:
            print("Enter new details (leave blank to keep unchanged):")
            event_name = input("Enter Event Name: ").strip()
            event_date = input("Enter Event Date (YYYY-MM-DD): ").strip()
            if event_date and not validate_date(event_date):
                print("Invalid date format. Skipping update for date.")
                event_date = record.get("event_date")
            event_description = input("Enter Event Description: ").strip()
            if event_name:
                record["event_name"] = event_name
            if event_date:
                record["event_date"] = event_date
            if event_description:
                record["event_description"] = event_description
            updated = True
    if updated:
        save_data_file("data/events.txt", records)
        print("Event updated successfully.")
    else:
        print("Event not found.")

def remove_event():
    print("\nRemove Event")
    event_id = input("Enter Event ID to remove: ").strip()
    records = load_data_file("data/events.txt")
    new_records = [record for record in records if record.get("event_id") != event_id]
    if len(new_records) == len(records):
        print("Event not found.")
    else:
        save_data_file("data/events.txt", new_records)
        print("Event removed successfully.")

def view_events():
    print("\nEvents:")
    records = load_data_file("data/events.txt")
    if not records:
        print("No event records found.")
    else:
        for record in records:
            print(record)

#communicationss
def manage_communication():
    while True:
        print("\nCommunication")
        print("1. Add Message")
        print("2. View Messages")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_message()
        elif choice == "2":
            view_messages()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def add_message():
    print("\nAdd Message")
    sender = input("Enter Sender Name: ").strip()
    if not sender:
        print("Sender name cannot be empty.")
        return
    message = input("Enter Message: ").strip()
    if not message:
        print("Message cannot be empty.")
        return
    record = {"sender": sender, "message": message}
    records = load_data_file("data/communication.txt")
    records.append(record)
    save_data_file("data/communication.txt", records)
    print("Message added successfully.")

def view_messages():
    print("\nMessages:")
    records = load_data_file("data/communication.txt")
    if not records:
        print("No messages found.")
    else:
        for record in records:
            print(f"{record.get('sender')}: {record.get('message')}")

