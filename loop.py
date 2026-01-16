# Match - case
# day = input("Enter a number: ")
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Looking for a valid day")


# day = input("Enter a number: ")
# match day:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Looking for a valid day")

# month = int(input("Enter a month: "))
# day = int(input("Enter a day: "))
# match month:
#     case 1:
#         print("January")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 2:
#         print("February")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 3:
#         print("March")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 4:
#         print("April")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 5:
#         print("May")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 6:
#         print("June")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 7:
#         print("July")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 8:
#         print("August")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")

#     case 9:
#         print("September")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 10:
#         print("October")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case 11:
#         print("November")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")

#     case 12:
#         print("December")
#         match day:
#             case 1 | 2 | 3 | 4 | 5 :
#                 print("Weekday")
#             case 6 | 7:
#                 print("Weekend")
#             case _:
#                 print("Looking for a valid day")
#     case _:
#         print("Looking for a valid month")

##LOOP 
# #for loop 
# number = [10,40,20,50,90,70,15]
# total = 0
# for num in number:
#     if num > 50:
#         print(num)
##range(start,stop,end)
# num= int(input("Enter a number: "))
# for num in range(0, num + 1,2):  
#     print(num)
    
# # While loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# #Break
# for num in range(1, 10):
#     if num == 5:
#         break Exit the loop when i is 5
#     print(num)

# i=0
# while i<10:
#     if i==5:
#         break
#     print(i)
#     i = i+1

#Continue
# for num in range(1, 10):
#     if num == 5:
#         continue # Skip the rest 
#     print(num)

##Pass
# for i in range(11,15):
#     if i == 12:
#         pass # Placeholder for future code
#     print(i)

# #list 
# a = [1,2,3,4,5]
# res = [num for num in a if num > 3]
# print(res)
# #Dictionary 
# a = {"name": "Alice", "age": 30, "city": "New York"}
# print(a)


# # An employee task manager has different users.
# user = input("Enter your role: ")
# match user:
#     case "Manager": 
#         print("assign tasks and view reports")
#     case "Admin":
#         print("manage employees and tasks")
#     case "Employee":
#         print("view and update your tasks")
#     case _:
#         print("invalid role")

# #An admin wants to view all tasks assigned to employees.
# tasks = ["Design logo", "Fix login bug", "Prepare report", "Update database"]
# print("Tasks assigned to employees:")
# for index,task in enumerate(tasks):
#     print(index,task)

# #An employee keeps completing tasks until no tasks are left.
# tasks = ["Task 1", "Task 2", "Task 3"]
# while tasks:
#     print("Current tasks:", tasks)
#     completed_task = input("Enter the completed task : ")
#     if completed_task in tasks:
#         tasks.remove(completed_task)
#         print(f"Completed: {completed_task}")
#     elif completed_task == 'quit':
#         break
#     else:
#         print("Invalid task.")
# print("All tasks completed!")

# #Only high priority tasks should be processed.
# tasks = [
#     ("Design UI", "low"),
#     ("Fix payment bug", "high"),
#     ("Update docs", "low"),
#     ("Deploy app", "high")
# ]
# print("High-priority tasks:")

# for task_name, priority in tasks:
#     if priority == "low":
#         pass        # future logic for low-priority tasks
#         continue    # skip low-priority tasks

#     print(task_name)

#tasks = [{"task": "Design UI", "status": "completed"},{"task": "Fix bug", "status": "pending"},{"task": "Testing", "status": "pending"},{"task": "Deploy", "status": "completed"}]
# # Write:
# # A list comprehension to get only pending task names
# # A set comprehension to get unique task statuses
# # A dict comprehension where task name is the key and status is the value
# task = [{"task": "Design UI","status": "completed"},
#           {"task": "Fix bug", "status": "pending"}
#           ,{"task": "Testing", "status": "pending"},
#           {"task": "Deploy", "status": "completed"}]
# pending_tasks = [t["task"] for t in task if t["status"] == "pending"]
# print("pending_tasks:", pending_tasks)
# statuses = {t["status"] for t in task}
# print("statuses:", statuses)
# task_status = {t["task"]: t["status"] for t in task}
# print("task_status:", task_status)

# #Take input status ("pending", "in-progress", "completed").
# # Using match-case, print:
# # pending → “Task not started”
# # in-progress → “Task is currently being worked on”
# # completed → “Task completed successfully”
# # default → “Invalid task status”

# status = input("Enter task status: ")
# match status :
#     case "pending":
#         print("Task not started")
#     case "in-progress":
#         print("Task is currently being worked on")
#     case "completed":
#         print("Task completed successfully")
#     case _:
#         print("Invalid task status")

# # Given:
# # tasks = [
# #     ("Design UI", "Design"),
# #     ("Fix server issue", "IT"),
# #     ("Prepare salary report", "Management"),
# #     ("Database backup", "IT")
# # ]
# # Using a for loop:
# # Skip tasks not belonging to "IT" using continue
# # Print only IT department task names

# tasks = [
#     ("Design UI", "Design"),
#    ("Fix server issue", "IT"),
#     ("Prepare salary report", "Management"),
#     ("Database backup", "IT")]

# for tasks_name,deparment in tasks:
#     if deparment != 'IT':
#         continue
#     print(tasks_name, ":", deparment)

# #Question:
# Using a while loop:
# Allow maximum 3 login attempts
# If correct pas is entered, print "Login successful" and break
# If attempts are over, print "Account locked"
# pa = "admin123"
# attempts = 3 
# while attempts > 0:
#     k = input("Enter password: ")
#     if k == pa:
#         print("Login successful")
#         break
#     else:
#         attempts = attempts - 1
#         print("Incorrect password. Try again.")
# if attempts == 0:
#     print("Account locked")

# # Create a function:
# # def notify_employee(task_status):
# # If status is "completed", print "Notification sent"
# # If status is "pending", use pass (feature to be added late
# task_status = input("Enter task status: ")
# def notify_employee(task_status):
#     if task_status == "completed":
#         print("Notification sent")
#     elif task_status == "pending":
#         pass   # feature to be added later
# # calling the function
# notify_employee("completed")
# notify_employee("pending")
