# class Employee:
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name

# emp1 = Employee(101, "Rahul")


# class Employee:
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name

# emp1 = Employee(101, "Rahul")

# print("id = ", emp1.emp_id)
# print("name = ", emp1.name)


# class Employee:
#     def __init__(self, emp_id, name, age=18):  #Default values 
#         self.emp_id = emp_id
#         self.name = name
#         self.age = age

# emp1 = Employee(101, "Rahul", 25)
# emp2 = Employee(102, "Raj")

# print("id = ", emp1.emp_id)
# print("name = ", emp1.name)
# print("age = ", emp1.age)
# print("id = ", emp2.emp_id)
# print("name = ", emp2.name)
# print("age = ", emp2.age)

# class Person:
#     def __init__(self,name,emp_id,email):
#         self.name = name 
#         self.emp_id = emp_id
#         self.email = email
# emp1 = Person("Rahul", 101, "rahul@example.com")
# emp2 = Person("Raj", 102, "raj@example.com")

# print("emp1 details:")
# print("Name:", emp1.name)
# print("Emp ID:", emp1.emp_id)
# print("Email:", emp1.email)

# print("emp2 details:")
# print("Name:", emp2.name)
# print("Emp ID:", emp2.emp_id)
# print("Email:", emp2.email)

# #Question:Create a class Employee with attributes: emp_id  name departmen

# class Employee:
#     def __init__(self,emp_id,name,department):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
# emp1 = Employee(101, "Rahul", "IT")
# emp2 = Employee(102, "Raj", "HR")

# print("emp1 details:")
# print("Emp ID:", emp1.emp_id)
# print("Name:", emp1.name)
# print("Department:", emp1.department)

# print("emp2 details:")
# print("Emp ID:", emp2.emp_id)
# print("Name:", emp2.name)
# print("Department:", emp2.department)

#Question:Create a class UserLogin with: email p Use __init__ to initialize these values.

class UserLogin:
    def __init__(self,email,p):
        self.email = email
        self.p = p

user = UserLogin("admin@example.com", "admin123")
print(f"Email: {user.email}, P: {user.p} logged in successfully")
