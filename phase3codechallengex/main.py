from models.department import Department
from models.employee import Employee

engineering = Department("Engineering")
hr = Department("HR")

e1 = Employee("Alice", 80000, engineering)
e2 = Employee("Bob", 70000, engineering)
e3 = Employee("Charlie", 60000, hr)

print(engineering.total_salary())        
print(engineering.average_salary())       
print(hr.average_salary())                


print(Employee.find_by_name("Alice"))    
print(Employee.find_by_id(2))             
