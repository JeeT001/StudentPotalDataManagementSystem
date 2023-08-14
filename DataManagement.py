import json
import datetime

# Data Structure Selection
students = []

# Creating Student Database
def load_students():
    with open('students.txt', 'r') as file:
        data = json.load(file)
        students.extend(data)

def save_students():
    with open('students.txt', 'w') as file:
        json.dump(students, file)

# Adding/Deleting Students
def add_student():
    student = {}
    # student['ID'] = generate_student_id(student)
    student['ID'] = generate_student_id(input("Enter your First Name For ID: "), input("Enter your Last Name for ID: "))
    student['Name'] = input("Enter student First Name: ")
    student['LName'] = input("Enter student Last Name: ")
    student['Email'] = input("Enter student email: ")
    student['Campus'] = input("Enter student campus: ")
    student['Subject'] = input("Enter Subject you want to study DSA, Match, IT: ")
    
    students.append(student)
    print("Student added successfully!")

def delete_student():
    student_id = input("Enter the ID of the student to delete: ")
    for student in students:
        if student['ID'] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")


def generate_student_id(first_name, last_name):
    
    first_three_chars = (first_name[:3] + last_name[:3]).upper()
    current_year = datetime.date.today().year
    student_id = f"{first_three_chars}{current_year}"

    return student_id

# Sorting Student Records
def sort_students_by_id():
    sorted_students = sorted(students, key=lambda x: x['ID'])
    display_students(sorted_students)

def sort_students_by_first_name():
    sorted_students = sorted(students, key=lambda x: x['Name'].split()[0])
    display_students(sorted_students)

def sort_students_by_last_name():
    sorted_students = sorted(students, key=lambda x: x['LName'].split()[-1])
    display_students(sorted_students)

def sort_students_by_campus():
    sorted_students = sorted(students, key=lambda x: x['Campus'])
    display_students(sorted_students)

# Searching Student Records
def search_student_by_id():
    student_id = input("Enter the ID of the student to search: ")
    search_results = [student for student in students if student['ID'] == student_id]
    display_students(search_results)

def search_student_by_first_name():
    first_name = input("Enter the first name of the student to search: ")
    search_results = [student for student in students if student['Name'].split()[0].lower() == first_name.lower()]
    display_students(search_results)

def search_student_by_last_name():
    last_name = input("Enter the last name of the student to search: ")
    search_results = [student for student in students if student['LName'].split()[-1].lower() == last_name.lower()]
    display_students(search_results)

# Utility function to display student records
def display_students(student_list):
    for student in student_list:
        print("ID:", student['ID'])
        print("First Name:", student['Name'])
        print("Last Name:", student['LName'])
        print("Email:", student['Email'])
        print("Campus:", student['Campus'])
        print("Subject:", student['Subject'])
        
        print()

# Menu
def main_menu():
    while True:
        print("Student Portal")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Sort Students")
        print("4. Search Students")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            sort_menu()
        elif choice == '4':
            search_menu()
        elif choice == '5':
            save_students()
            break
        else:
            print("Invalid choice.Please try again.")

# Sub-menu for sorting options
def sort_menu():
    while True:
        print("Sort Students")
        print("1. By ID")
        print("2. By First Name")
        print("3. By Last Name")
        print("4. By Campus")
        print("5. Back to Main Menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            sort_students_by_id()
        elif choice == '2':
            sort_students_by_first_name()
        elif choice == '3':
            sort_students_by_last_name()
        elif choice == '4':
            sort_students_by_campus()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Sub-menu for searching options
def search_menu():
    while True:
        print("Search Students")
        print("1. By ID")
        print("2. By First Name")
        print("3. By Last Name")
        print("4. Back to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            search_student_by_id()
        elif choice == '2':
            search_student_by_first_name()
        elif choice == '3':
            search_student_by_last_name()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Step 8: Store and Retrieve Data from TXT Files which is stored as student.txt
load_students()
main_menu()
