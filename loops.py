# #students = ["Biswa","Deb", "Satish","Sita","Ram","Sita"]
# students_detail = {
#     "name" : "Biswa",
#     "age" : "35",
#     "place" : "Bangalore"
# }
# for item  in students_detail:
#     print(students_detail[item])


all_students = {
    "biswa" : {
        "name" : "Biswa",
        "age" : 35,
        "place" : "Bangalore"
    },
    "Deb" : {
        "name" : "Deba",
        "age" : 25,
        "place" : "BBSR"
    }
}

for item in all_students:
    print(all_students[item].keys())


