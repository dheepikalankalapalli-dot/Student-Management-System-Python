import json

FILE_NAME = "students.json"


try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
except:
    students = {}


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    students[roll] = {"name": name, "marks": marks}
    save_data()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No records found")
    else:
        for roll, data in students.items():
            print("Roll:", roll, "| Name:", data["name"], "| Marks:", data["marks"])


def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found")


def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new name: ")
        marks = input("Enter new marks: ")
        students[roll] = {"name": name, "marks": marks}
        save_data()
        print("Student updated successfully!")
    else:
        print("Student not found")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        save_data()
        print("Student deleted successfully!")
    else:
        print("Student not found")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Program exited")
        break
    else:
        print("Invalid choice")
