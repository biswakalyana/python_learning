students = {
    "Sateesh": {"Mathematics": 95, "Science": 90, "History": 72, "Geograpy":85,"Literature": 65},
    "Guru" :  {"Mathematics": 90, "Science": 90, "History": 66, "Geograpy":52,"Literature": 23},
    "Sonali":  {"Mathematics": 23, "Science": 32, "History": 72, "Geograpy":53,"Literature": 35},
    "Puja":  {"Mathematics": 98, "Science": 95, "History": 88, "Geograpy":85,"Literature": 78},
    "Varun":  {"Mathematics": 65, "Science": 75, "History": 62, "Geograpy":45,"Literature": 66}
}
'''
subjects = list(next(iter(students.values())).keys())
'''
print(next(iter(students.values())).keys())