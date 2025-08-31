"""
Exercise Title: Student Grades Analyzer
📘 Problem Statement:
You are building a simple program to analyze student grades. The program should:
    Ask the user to input the number of students.
    For each student:
        Ask for their name.
        Ask for their grade (as a string, but convert it to a number).
        Store the data in a dictionary, where the key is the student name and the value is their grade.
    Add all grades to a list.
    After all data is entered:
        Print all student names and their grades.
        Print the average grade.
        Print the highest and lowest grade.
        Print a list of students who passed (grade >= 50).
"""
## Initialize variables
all_students_grades = []
all_students = {}
pass_grade = 5

## Take user inputs of all stidents
number_of_students = int(input("Enter number of students in class : "))
counter = number_of_students
while counter > 0:
    name = input("Enter name of student - ")      
    grade = int(input("Enter grade of student - "))
    all_students[name] = grade # create dictionary in this format - { "biswa" : 5 , "deb" : 7, "Chinta":6 }
    # all_students[counter] = {  # create dictionary in this format - { 1: {"biswa" : 5} , 2: {"deb" : 7}, 3: {"Chinta":6} }
    #     "name" : name,
    #     "grade" : grade
    # }
    all_students_grades.append(grade) # Add all grades to a list
    counter = counter-1

## Print all student names and their grades.
for student in all_students :
    print(f"Grade of Student {student} is {all_students[student]}")

## Average 
average = sum(all_students_grades) / len(all_students_grades)
print(f"Avergae grade of all students = {average}")

## Max and Min
max_grade = max(all_students_grades)
min_grade = min(all_students_grades)
print(f"Minimum grade among all students is - {min_grade}")
print(f"Maximum grade among all students is - {max_grade}")

## Find which students have scored max grade ?
# all_students = {
# 'Biswa': 4, 
# Ram': 5, 
# 'Deb': 9, 
# 'Chint': 7, 
# 'Gopal': 9}
# max_grade = 9
print(f"Students who have scored maximum grade, i.e. {max_grade} ")
for name in all_students:
    if (all_students[name] == max_grade): ## 9 ==9
        print(name)

## FInd students whose grade is greater than 5
print(f"Students who have scored more than pass grade, i.e. {pass_grade} ")
for name in all_students:
    if (all_students[name] >= pass_grade): 
        print(name)