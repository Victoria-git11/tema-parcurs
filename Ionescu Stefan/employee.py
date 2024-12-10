class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary


class Manager(Employee):
    """Manager class inheriting from Employee"""
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"Echipa {department}"
        Manager.mgr_count += 1
 # Creating Employee objects
empl1 = Employee("Vlad Andrei", 6000)
empl2 = Employee("Apostu George", 8500)
empl3 = Employee("Ionescu Andrei", 9000)
empl4 = Employee("Niculescu Mihaela ", 400000)
empl5 = Employee("Popescu Maria", 1000000)

    
# Creating Manager objects
manager1 = Manager("Ionescu Andrei", 70000, "IT")
manager2 = Manager("Pop Nicolaie", 3500, "Human Resources")
manager3 = Manager("Badea Vlad", 7000, "Informatica")
manager4 = Manager("Alexe Gabriela ", 40000, "Human Resources")
manager5 = Manager("Baciu Andreea", 650000, "IT")

# Salary Out
manager1.display_employee()
empl2.display_employee()

# Nr of elements
print(f"Number of Employee objects: {Employee.empCount}")
print(f"Number of Manager objects: {Manager.mgr_count}")

        

