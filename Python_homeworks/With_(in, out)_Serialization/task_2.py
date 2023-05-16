# In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],
# in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...].
# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create
# csv file in format:
# header line - name, department
# next lines :  <userName>, <departmentName>
# If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.
# Create appropriate json-schemas for user and department.
# If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception
# To validate instances create function validate_json(data, schema)

import json
import jsonschema
from jsonschema import validate
import csv
user = {"type": "object",
        "required": ["id", "name", "department_id"]}

department = {"type": "object",
              "required": ["id", "name"]}

class DepartmentName(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Department with id {self.data} doesn't exists"

class InvalidInstanceError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Error in {self.data} schema"


def user_with_department(csv_file, user_json, department_json):
    with open(user_json, "r") as fu:
        user_data = json.load(fu)
    with open(department_json, "r") as fd:
        department_data = json.load(fd)
    field_user_id = [i["department_id"] for i in user_data if validate_json(i, user, "user")]
    field_department_id = [e["id"] for e in department_data if validate_json(e, department, "department")]
    for i in field_user_id:
        if i not in field_department_id:
            raise DepartmentName(f"{i}")
    data = [[e["name"], i["name"]] for e in user_data for i in department_data if e['department_id'] == i["id"]]
    with open(csv_file, mode="w", newline='') as fc:
        writer = csv.writer(fc, delimiter=",")
        writer.writerow(["name", "department"])
        for i in data:
            writer.writerow(i)

def validate_json(data, schema, typ):
    try:
        validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(typ)
    return True

#Tests

try:
  user_with_department("user_department.csv", "user_without_dep.json", "department.json")
except DepartmentName as e:
    print(str(e))
#Expect
# Department with id 20 doesn't exists

user_with_department("user_department.csv", "user.json", "department.json")
print_file("user_department.csv")
#Expect
# name,department
# userName,Dep 1
# userName2,Dep 1
# userName3 From Dep 2,Dep 2
# userName4 from Dep 1,Dep 1
# userName4 without Dep,Dep 2

try:
  user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
except InvalidInstanceError as e:
    print(str(e))
#Expect Error in user schema

try:
  user_with_department("user_department.csv", "user.json", "department_without_id.json")
except InvalidInstanceError as e:
    print(str(e))
#Expect Error in department schema