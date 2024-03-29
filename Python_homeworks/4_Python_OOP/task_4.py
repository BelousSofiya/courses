# Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper
# and to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes are ' \
# in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself! Create another class called Student and do
# the following:
# Create an attribute called tests_taken and set the default as  'No tests taken'.
# Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers.
# Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way as
# shown in the point below.
# Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen in the
# examples below (whether or not the student has failed, and their percentage in brackets).
# Example:
#
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
#
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
#
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, a, lst_marks):
        if type(self.tests_taken) == str:
            self.tests_taken = {}
        lst = [1 for i, e in enumerate(a.markscheme) if e == lst_marks[i]]
        percent = round((len(lst)*100)/len(a.markscheme))
        if percent >= int(a.pass_mark[0:2]):
            self.tests_taken[a.subject] = f"Passed! ({percent}%)"
        else:
            self.tests_taken[a.subject] = f"Failed! ({percent}%)"

#Tests

paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
student1 = Student()
print(student1.tests_taken)
student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
print(student1.tests_taken)
print(paper1.subject)
print(paper1.markscheme)
print(paper1.pass_mark)
#Expect
# No tests taken
# {'Maths': 'Passed! (80%)'}
# Maths
# ['1A', '2C', '3D', '4A', '5A']
# 60%

paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
student2 = Student()
student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
print(student2.tests_taken)
print(paper2.subject)
print(paper2.markscheme)
print(paper2.pass_mark)
#Expect
# {'Chemistry': 'Failed! (25%)'}
# Chemistry
# ['1C', '2C', '3D', '4A']
# 75%

paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
student2 = Student()
student3 = Student()
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
print(paper3.subject)
print(paper3.markscheme)
print(paper3.pass_mark)
#Expect
# No tests taken
# {'Maths': 'Failed! (20%)', 'Computing': 'Failed! (43%)'}
# Computing
# ['1D', '2C', '3C', '4B', '5D', '6C', '7A']
# 75%

student3 = Student()
paper4 = Testpaper('Physics', ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A'], '90%')
student3.take_test(paper4, ['1A', '2C', '3A', '4C', '5D', '6C', '7B', '8C', '9D', '10A', '11A'])
print(student3.tests_taken)
print(paper4.subject)
print(paper4.markscheme)
print(paper4.pass_mark)
#Expect
# {'Physics': 'Failed! (73%)'}
# Physics
# ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A']
# 90%
