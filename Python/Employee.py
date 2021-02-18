
# Employee, WageEmployee and SalaryEmployee classes for the O.O.P. TEST #

# Employee Class #
   # Attributes: fname, lname, employeeID #

class Employee:

    def __init__(self, first_name, last_name, employee_ID):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_ID = employee_ID

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name} ({self.employee_ID})"

# WageEmployee Class
    # Attributes: fname, lname, employeeID, hourly wage, weekly hours

class WageEmployee(Employee):

    def __init__(self, first_name, last_name, employee_ID, hourly_wage, weekly_hours):
        super().__init__(first_name, last_name, employee_ID)
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours

    def weekly_earnings(self):
        return (self.hourly_wage * self.weekly_hours)

    def __str__(self):
        return f"Wage Employee: {self.first_name} {self.last_name} ({self.employee_ID}) WEEKLY EARNINGS:" \
               f" {self.weekly_earnings()}"

# SalaryEmployee Class
    # Attributes: fname, lname, employeeID, Salary

class SalaryEmployee(Employee):
    
    def __init__(self, first_name, last_name, employee_ID, salary):
        super().__init__(first_name, last_name, employee_ID)
        self.salary = salary

    def weekly_earnings(self):
        return (self.salary // 52.1429)

    def __str__(self):
        return f"Salary Employee: {self.first_name} {self.last_name} ({self.employee_ID}) WEEKLY EARNINGS:" \
               f" {self.weekly_earnings()}"


Employee1 = Employee("Ronnie", "McDonnie", 20109408)
WageEmployee1 = WageEmployee("Donnie", "McDonnie", 20108888, 25.00, 40)
SalaryEmployee1 = SalaryEmployee("Peter", "Piper", 20106666, 800000)

print(Employee1)
print(WageEmployee1)
print(SalaryEmployee1)


    