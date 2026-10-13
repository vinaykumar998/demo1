# Student Marks Calculator


name = input("Enter student name: ")

mark1 = float(input("Enter marks in Subject 1 (out of 100): "))
mark2 = float(input("Enter marks in Subject 2 (out of 100): "))
mark3 = float(input("Enter marks in Subject 3 (out of 100): "))

total = mark1 + mark2 + mark3
average = total / 3
percentage = (total / 300) * 100

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n----- STUDENT MARKS REPORT -----")
print("Student Name:", name)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)
print("Total Marks:", total, "/ 300")
print("Average Marks:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Result:", result)