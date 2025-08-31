def calculate(number1, number2, number3=5):
    total = number1 + number2 + number3
    #print(total)
    return total

score_in_math = 40
score_in_science = 80
total_score = calculate(score_in_math, score_in_science, 80)
print(total_score)

def compare(number1, number2):
    if number1 > number2:
        return "first number is large"
    else:
        return "second number is large"

print(compare(40,40))

def total_score(*scores):
    return sum(scores)

students_score = {
    "biswa" : {
        "math" : 30,
        "science" : 40
    },
    "deb" : {
        "math" : 30,
        "science" : 40,
        "history" : 45
    },
    "sateesh" : {
        "math" : 40,
        "science" : 50,
        "history" : 75,
        "lit" : 45
    }
}    

biswa_score = total_score(30, 40)
print(biswa_score)
deb_score = total_score(30,40,45)
print(deb_score)
sat_score = total_score(40, 50, 75, 45)
print(sat_score)