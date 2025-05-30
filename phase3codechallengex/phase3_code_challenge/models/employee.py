class Employee:
    all = []
    _id_counter = 1

    def __init__(self, name, salary, department):
        self.id = Employee._id_counter
        self.name = name
        self.salary = salary
        self.department = department
        Employee._id_counter += 1
        Employee.all.append(self)

    def __repr__(self):
        return f"<Employee {self.id}: {self.name}, ${self.salary}, Dept: {self.department.name}>"
