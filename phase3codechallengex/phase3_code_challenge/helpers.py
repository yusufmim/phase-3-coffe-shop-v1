from models.department import Department
from models.employee import Employee

def exit_program():
    print("Goodbye!")
    exit()

def list_departments():
    for dept in Department.all:
        print(dept)

def find_department_by_name():
    name = input("Enter department name: ")
    for dept in Department.all:
        if dept.name == name:
            print(dept)
            return
    print("Department not found.")

def find_department_by_id():
    try:
        id = int(input("Enter department ID: "))
        for dept in Department.all:
            if dept.id == id:
                print(dept)
                return
        print("Department not found.")
    except ValueError:
        print("Invalid ID.")

def create_department():
    name = input("Enter new department name: ")
    Department(name)
    print(f"Department '{name}' created.")

def update_department():
    try:
        id = int(input("Enter department ID to update: "))
        for dept in Department.all:
            if dept.id == id:
                new_name = input("Enter new name: ")
                dept.name = new_name
                print("Department updated.")
                return
        print("Department not found.")
    except ValueError:
        print("Invalid ID.")

def delete_department():
    try:
        id = int(input("Enter department ID to delete: "))
        for dept in Department.all:
            if dept.id == id:
                Department.all.remove(dept)
                print("Department deleted.")
                return
        print("Department not found.")
    except ValueError:
        print("Invalid ID.")

def list_employees():
    for emp in Employee.all:
        print(emp)

def find_employee_by_name():
    name = input("Enter employee name: ")
    for emp in Employee.all:
        if emp.name == name:
            print(emp)
            return
    print("Employee not found.")

def find_employee_by_id():
    try:
        id = int(input("Enter employee ID: "))
        for emp in Employee.all:
            if emp.id == id:
                print(emp)
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid ID.")

def create_employee():
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    department_id = int(input("Enter department ID: "))
    for dept in Department.all:
        if dept.id == department_id:
            Employee(name, salary, dept)
            print("Employee created.")
            return
    print("Department not found.")

def update_employee():
    try:
        id = int(input("Enter employee ID to update: "))
        for emp in Employee.all:
            if emp.id == id:
                emp.name = input("Enter new name: ")
                emp.salary = float(input("Enter new salary: "))
                print("Employee updated.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def delete_employee():
    try:
        id = int(input("Enter employee ID to delete: "))
        for emp in Employee.all:
            if emp.id == id:
                Employee.all.remove(emp)
                print("Employee deleted.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid ID.")

def list_department_employees():
    try:
        id = int(input("Enter department ID: "))
        for dept in Department.all:
            if dept.id == id:
                for emp in dept.employees():
                    print(emp)
                return
        print("Department not found.")
    except ValueError:
        print("Invalid ID.")
