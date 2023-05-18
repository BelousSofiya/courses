# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
# Make both classes JSON serializable.
# Json-files represent information about student (students).
# Create methods:
# Student.from_json(json_file) that return Student instance from attributes from json-file;
# Student.serialize_to_json(filename)
# Group.serialize_to_json(list_of_groups, filename)
# Group.create_group_from_file(students_file)
# Parse given files, create instances of Student class and create instances of Group class (title for group is name of
# json-file without extension).


import json
class Student:
    def __init__(self, full_name:str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, "r") as f:
            dict_args = json.load(f)
        return cls(dict_args["full_name"], dict_args["avg_rank"], dict_args["courses"])

    def serialize_to_json(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self, default=lambda o: o.__dict__))

class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        stud = [i.__str__() for i in self.students]
        return f"{self.title}: {stud}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(list_of_groups, default=lambda o: o.__dict__))

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file, "r") as f:
            dict_args = json.load(f)
            students = [Student(**dict_args)] if type(dict_args) == dict else [Student(**i) for i in dict_args]
            return cls(students_file.split(".")[0], students)

user1 = Student.from_json("2020-01.json")
print(user1)
#Expect
# Student2 from group2 (50.4): ['C++']

user1 = Student.from_json("2020-01.json")
Student.serialize_to_json(user1, "test_student.json")
print_file("test_student.json")
#Expect
# {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}

import json
with open("2020_2.json") as read_file:
     user2 = json.load(read_file)
print([str(Student(**item)) for item in user2])
#Expect
# ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]

g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2],"g1")
print_file("g1")
#Expect
# [{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]

g1 = Group.create_group_from_file("2020_2.json")
print(g1)
#Expect
# 2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]

g2 = Group.create_group_from_file("2020-01.json")
print(g2)
#Expect 2020-01: ["Student2 from group2 (50.4): ['C++']"]