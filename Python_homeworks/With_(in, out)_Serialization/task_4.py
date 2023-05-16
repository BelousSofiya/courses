# Create context manager class SerializeManager with attributes filename and type for serializing python object to
# different formats.
# This class should contain method serialize for serialize object to filename according to  type.
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.
# For example:
# if user_dict = { 'name': 'Roman', 'id': 8}
# then
# serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
# serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"


import json
import pickle
from enum import Enum


FileType = Enum('FileType', ['JSON', 'BYTE'])

class SerializeManager:
    def __init__(self, filename, type):
        self.filename = filename
        self.type = type

    def serialize(self, obj):
        if self.type == FileType.JSON:
            with open(self.filename, "w") as f:
                json.dump(obj, f)
        elif self.type == FileType.BYTE:
            with open(self.filename, "bw") as f:
                pickle.dump(obj, f)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass
def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


print(isinstance(serialize.__globals__['SerializeManager'], object))
#Expect
# True

print(issubclass(FileType, Enum))
#Expect
# True

from os import path

print (str(path.exists('1')))
serialize("String", "1", FileType.JSON)
print (str(path.exists('1')))
#Expect
# False
# True

user_dict = {"name": "Hallo", "id" : 2}
serialize(user_dict, "2", FileType.BYTE)
with open("2", "rb") as file:
  print(pickle.load(file))
#Expect {'name': 'Hallo', 'id': 2}

user_dict = {"name": "Hallo", "id" : 2}
serialize(user_dict, "2", FileType.JSON)
print_file("2")
#Expect {"name": "Hallo", "id": 2}

data = {"prop1": "value1", "prop2" : "value2"}
with SerializeManager("test_4.json", FileType.JSON) as user:
    user.serialize(data)
print_file("test_4.json")
#Expect {"prop1": "value1", "prop2": "value2"}