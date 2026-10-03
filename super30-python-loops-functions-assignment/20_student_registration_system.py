# Q20: Student Registration System
# DICTIONARY (id -> record) for fast lookup by ID, FUNCTIONS for each feature,
# FOR loops to iterate records, WHILE loop for the menu.
# Build a menu-driven application using functions + for loops + while loops. 
# The system should allow users to add a student, 
# view all students, search by ID, update student details, delete a student, 
# calculate class average marks, display the highest-performing student, and exit. 
# Store the records using appropriate Python data structures

students = {}   # {id: {"name": str, "age": int, "marks": float}}


def add_student():
    sid = input("Student ID: ").strip()
    if sid in students:
        print("ID already exists.")
        return
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks (0-100): "))
    if not 0 <= marks <= 100:
        print("Invalid marks.")
        return
    students[sid] = {"name": name, "age": age, "marks": marks}
    print("Student added.")


def view_all():
    if not students:
        print("No students registered.")
        return
    for sid, s in students.items():
        print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")


def search_student():
    sid = input("Enter ID to search: ").strip()
    s = students.get(sid)
    if s:
        print(f"Found -> {sid}: {s['name']}, Age {s['age']}, Marks {s['marks']}")
    else:
        print("Student not found.")


def update_student():
    sid = input("Enter ID to update: ").strip()
    if sid not in students:
        print("Student not found.")
        return
    name = input("New name (blank to keep): ")
    age = input("New age (blank to keep): ")
    marks = input("New marks (blank to keep): ")
    if name:
        students[sid]["name"] = name
    if age:
        students[sid]["age"] = int(age)
    if marks:
        students[sid]["marks"] = float(marks)
    print("Updated.")


def delete_student():
    sid = input("Enter ID to delete: ").strip()
    if sid in students:
        del students[sid]
        print("Deleted.")
    else:
        print("Student not found.")


def class_average():
    if not students:
        print("No students.")
        return
    total = 0
    for s in students.values():
        total += s["marks"]
    print(f"Class average: {total / len(students):.2f}")


def top_student():
    if not students:
        print("No students.")
        return
    best_id = None
    for sid, s in students.items():
        if best_id is None or s["marks"] > students[best_id]["marks"]:
            best_id = sid
    b = students[best_id]
    print(f"Top performer: {b['name']} (ID {best_id}) with {b['marks']} marks")


while True:
    print("\n1.Add 2.View All 3.Search 4.Update 5.Delete 6.Class Avg 7.Top Student 8.Exit")
    choice = input("Choose: ")
    try:
        if choice == "1": add_student()
        elif choice == "2": view_all()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": class_average()
        elif choice == "7": top_student()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input, please enter numbers where required.")
