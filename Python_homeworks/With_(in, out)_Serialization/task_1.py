# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records
# (unique by key "name") by merging information from all input_files argument (if we find user with already existing name
# from previous file we should ignore it). Use pretty printing for writing users to json-file.
# If the function cannot find input files we need to log information with error level
# root - ERROR - File <file name> doesn't exist
#
# For example:
# user1.json :
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]
#
# user2.json :
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]
#
# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    res = []
    content = []
    for i in input_files:
        try:
            with open(i, "r") as f:
                content += json.load(f)
        except FileNotFoundError:
            logging.error(f"File {i} doesn't exist")
    name_value = list(set([i["name"] for i in content if "name" in i]))
    for i in content:
        if "name" in i:
            if i["name"] in name_value:
                res.append(i)
                name_value.remove(i["name"])
    with open(output_file, "w") as f:
        f.write(json.dumps(res, indent=4))

#Tests

parse_user("user4.json", "user1.json", "user2.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob1",
#         "languages": [
#             "English",
#             "French"
#         ]
#     },
#     {
#         "name": "Bob2",
#         "languages": [
#             "English",
#             "French"
#         ]
#     },
#     {
#         "name": "Bob",
#         "languages": [
#             "English",
#             "Fench"
#         ]
#     }
# ]

parse_user("user4.json", "user_without_name.json")
print_file("user4.json")
#Expect
# []

parse_user("user4.json", "user_with_duplicated_name.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob1",
#         "rate": 25,
#         "languages": [
#             "English",
#             "French"
#         ]
#     }
# ]

parse_user("user4.json", "user_with_duplicated_name.json", "user_n.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob1",
#         "rate": 25,
#         "languages": [
#             "English",
#             "French"
#         ]
#     }
# ]

parse_user("user4.json", "user2.json", "user1.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob",
#         "languages": [
#             "English",
#             "Fench"
#         ]
#     },
#     {
#         "name": "Bob2",
#         "languages": [
#             "English",
#             "Fench"
#         ]
#     },
#     {
#         "name": "Bob1",
#         "languages": [
#             "English",
#             "French"
#         ]
#     }
# ]

parse_user("user4.json", "user_.json", "user_n.json")
print_file("user4.json")
#Expect
# []

print_file("app.log")
#Expect
# root - ERROR - File user_n.json doesn't exist
# root - ERROR - File user_.json doesn't exist
# root - ERROR - File user_n.json doesn't exist

parse_user("user4.json", "user3a.json", "user3b.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob1",
#         "languages": [
#             "English"
#         ]
#     },
#     {
#         "name": "Common User",
#         "languages": [
#             "German",
#             "Ukrainian"
#         ]
#     },
#     {
#         "name": "Bob2",
#         "languages": [
#             "English"
#         ]
#     }
# ]

parse_user("user4.json", "user3b.json", "user3a.json")
print_file("user4.json")
#Expect
# [
#     {
#         "name": "Bob2",
#         "languages": [
#             "English"
#         ]
#     },
#     {
#         "name": "Common User",
#         "languages": [
#             "Italian"
#         ]
#     },
#     {
#         "name": "Bob1",
#         "languages": [
#             "English"
#         ]
#     }
# ]