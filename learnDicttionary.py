# ## Dictionary
# students_detail = {
#     "name" : "Biswa",
#     "age" : "35",
#     "place" : "Bangalore"
# }
# print(students_detail["name"])

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
# print(all_students)
print(all_students["biswa"].keys())


# all_students_detail = {
#     "names" : ["Biswa","Deb", "Satish","Sita","Ram","Sita"],
#     "place_of_births" : ["Bangalore", "bbsr", "bbsr", "chennai","delhi"]
# }
# print(all_students_detail["names"])