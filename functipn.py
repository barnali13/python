# def evenodd(n):
#     if (n % 2 == 0) :
#         return "even"
#     else:
#         return "odd"    
# print(evenodd(5))
# print(evenodd(4))

# #Default Arguments  
# def evenodd(n, check_even=True):
#     if check_even:
#         return "even" if n % 2 == 0 else "odd"
#     else:
#         return "odd" if n % 2 == 0 else "even"
# n = int(input('Enter a number: '))
# print(evenodd(n))

# # Key Arguments 
# def employee(name, age, department): # without keyword arguments  order must be currect
#     print(f"Name: {name}, Age: {age}, Department: {department}")

# employee(name="Alice", age=30, department="HR")
# employee(name="Bob", age=25, department="IT")
# employee(name="Charlie", age=35, department="Finance")
# employee(department="HR", age=25, name="David")  


# def assign_task(task, priority="medium" , status="pending"):
#     print(f"Task: {task}, Priority: {priority}, Status: {status}")
# assign_task("Fix bug")
# assign_task("Fix bug", priority="high")
# assign_task("Fix bug", status="completed", priority="high")


# #positionl Arugements   #function based on their position (order)
# def employee(name, age, department):
#     print(f"Name: {name}, Age: {age}, Department: {department}")

# employee("Alice", 30, "HR")

# def show_numbers(*args):
#     print(args)

# show_numbers(10, 20, 30,40,50,60,70)

# def add(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     print(total)
# add(10,20,30,40,50,60,70)

# # Kwargs 
# def employee_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# employee_details(name ='Barnali', dept='IT',role =' Developer')

# def assign_task(employee,*tasks,**details):
#     print(f"Employee: {employee}")
#     for task in tasks:
#         print(f"Task: {task}")
#     for key, value in details.items():
#         print(f"{key}: {value}")

# assign_task(
#         'Barnali',
#         'Fix bug',
#         priority='high',
#         status='in progress'    )
