class Employee:
    """This class creates workers"""

    workers_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.workers_counter += 1
        return super().__new__(cls)

    def __init__(self, name, salary):
        self.validate_name(name)
        self.validate_salary(salary)
        self.__name = name
        self.__salary = salary

    @classmethod
    def __del__(cls):
        cls.workers_counter -= 1

    @staticmethod
    def validate_name(name):
        if type(name) != str:
            raise TypeError("Name has to be a string!")
        if len(name) < 3:
            raise ValueError("Too short name!")

    @staticmethod
    def validate_salary(salary):
        if type(salary) not in [int, float]:
            raise TypeError("Salary has to be an integer or float number!")
        if salary <= 0:
            raise ValueError("Invalid value of salary!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
       self.__salary = salary

    @classmethod
    def info(cls):
        info_dict = {"base_class": cls.__base__, "namespace": cls.__dict__,
                     "name": cls.__name__, "module name": cls.__module__, "documents": cls.__doc__}
        for i in info_dict.items():
            print(*i)

Employee.info()
a = Employee("John", 45.7)
b = Employee("Mark", 50)
c = Employee("Jane", 25)
print(a.name)
print(b.salary)
b.salary = 250
print(b.salary)
print(b.workers_counter)
del c
print(Employee.workers_counter)
d = c = Employee("Ann", 70)
print(b.workers_counter)
