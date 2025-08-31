students = {
    "Sateesh": {"Mathematics": 95, "Science": 90, "History": 27, "Geograpy":85,"Literature": 65},
    "Guru" :  {"Mathematics": 90, "Science": 90, "History": 66, "Geograpy":52,"Literature": 23},
    "Sonali":  {"Mathematics": 23, "Science": 32, "History": 72, "Geograpy":53,"Literature": 35},
    "Puja":  {"Mathematics": 89, "Science": 95, "History": 68, "Geograpy":85,"Literature": 78},
    "Varun":  {"Mathematics": 65, "Science": 75, "History": 62, "Geograpy":45,"Literature": 66}
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

for student_name, all_scores in students.items():
    total = calculate_total(all_scores)
    grade = calculate_grade(all_scores)
   
    student_totals[student_name]= total
    student_grades[student_name]= grade
   
    print(f"{student_name}-> Total Marks:{total}, Grade:{grade}")
   
print("\n----subject-wise Toppers----")
subjects = list(next(iter(students.values())).keys())

for subject in subjects:
    top_score = 0
    top_student = None
    for student_name, all_scores in students.items():
        score = all_scores[subject]
        if score > top_score:
            top_score = score
            top_student = student_name
    
    print(f"{subject} Topper: {top_student} {top_score} marks)")
