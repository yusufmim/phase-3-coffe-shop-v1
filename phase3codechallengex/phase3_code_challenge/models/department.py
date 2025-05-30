class Department:
    all = []
    _id_counter = 1

    def __init__(self, name):
        self.id = Department._id_counter
        self.name = name
        Department._id_counter += 1
        Department.all.append(self)

    def employees(self):
        return [e for e in Employee.all if e.department == self]

    def __repr__(self):
        return f"<Department {self.id}: {self.name}>"

from models.employee import Employee
