
### Person class with first and last name attributes ###

class Person:

    def __init__(self, first_name, last_name):    
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):                    
        return str(self.first_name) + str(self.last_name)

### Employee Class referencing the Person class for the first and last name values ###
 
class Employee(Person):

    def __init__(self, first_name, last_name, employee_number, salary):
        self.fullname = Person(first_name, last_name)
        self.employee_number = employee_number
        self.salary = salary
    
    def __str__(self):
        return str(self.fullname) + "employee #: " + str(self.employee_number) + "Salary: " + str(self.salary) 

    def raise_amt(self):
        return (self.salary * 0.05)

### Student class also referencing the Person class for the first and last name values ###

class Student(Person): 

    def __init__(self, first_name, last_name, student_number, current_courses):
        self.fullname = Person(first_name, last_name)
        self.student_number = student_number
        self.current_courses = current_courses
    
    def __str__(self):
        return str(self.fullname) + "studnet #: ", + str(self.student_number) + "Current Courses: ", + str(self.current_courses) 
    
    def DropCourse(self):
        Course_dropped = input("enter the course you want to drop")
        for value in self.current_courses:
            if Course_dropped == value:
                del value
                return self.current_courses
        
    def AddCourse(self):
        Course_added = input("enter the course you want to add")
        for value in self.current_courses:
            if Course_added != self.current_courses:
                self.current_courses + Course_added
                return self.current_courses




    
        



        