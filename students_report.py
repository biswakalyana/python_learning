students = {
    "Sateesh": {"Mathematics": 95, "Science": 90, "History": 72, "Geograpy":85,"Literature": 65,"Computer": 76},
    "Guru" :  {"Mathematics": 90, "Science": 90, "History": 66, "Geograpy":52,"Literature": 23,"Chemistry": 35},
    "Sonali":  {"Mathematics": 23, "Science": 32, "History": 72, "Geograpy":53,"Chemistry": 35,"Literature": 66},
    "Puja":  {"Mathematics": 98, "Science": 95, "History": 88, "Geograpy":85,"Literature": 78,"Computer": 86,"Physics": 66},
    "Varun":  {"Mathematics": 65, "Science": 75, "History": 62, "Geograpy":45,"Literature": 66,"Computer": 66}
}

def calculate_total(marks):
    return sum(marks.values())

def calculate_grade(marks):
    total = calculate_total(marks)
    if any(score < 30 for score in marks.values()) or total < 200:
        return "Failed"
    elif total>400:
        return "Outstanding"
    elif total>300:
        return "Good"
    else:
        return "Passed"
   
print("----Students Report----")
student_totals = {}
student_grades= {}

for student, subjects in students.items():
    total = calculate_total(subjects)
    grade = calculate_grade(subjects)
   
    student_totals[student]= total
    student_grades[student]= grade
   
    print(f"{student}-> Total Marks:{total}, Grade:{grade}")
   
print("\n----subject-wise Toppers----")
'''
subjects = list(next(iter(students.values())).keys())
'''
subjects = { subject
             for record in students.values()
             for subject in record.keys()
    }
print(subjects)
'''
for subject in subjects:
    topper = max(students, key=get_marks)
    print(f"{subject} Topper: {topper} ({students[topper][subject]}marks)")
'''