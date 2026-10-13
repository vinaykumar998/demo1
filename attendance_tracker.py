
import csv
import os

FILE_NAME = "attendance.csv"

# Load existing attendance records
students = {}

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students[row["Name"]] = row["Attendance"].split(",")


def save_attendance():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Attendance"])

        for name, records in students.items():
            writer.writerow([name, ",".join(records)])


def add_student():
    name = input("Enter student name: ").strip()

    if name and name not in students:
        students[name] = []
        print("Student added successfully!")
    elif name in students:
        print("Student already exists.")
    else:
        print("Name cannot be empty.")


def mark_attendance():
    name = input("Enter student name: ").strip()

    if name not in students:
        print("Student not found. Please add the student first.")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        students[name].append("Present")
        print("Marked as Present.")
    elif status == "A":
        students[name].append("Absent")
        print("Marked as Absent.")
    else:
        print("Invalid choice.")

    save_attendance()


def display_attendance():
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Attendance List ---")

    for name, records in students.items():
        total = len(records)
        present = records.count("Present")

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("Name:", name)
        print("Attendance:", records)
        print("Present:", present)
        print("Total Classes:", total)
        print("Attendance Percentage:", round(percentage, 2), "%")
        print("------------------------")


while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. Display Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        save_attendance()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        display_attendance()

    elif choice == "4":
        save_attendance()
        print("Attendance saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
