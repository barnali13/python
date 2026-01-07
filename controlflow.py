# #if-else  Statements
# #3.Check if a person is eligible to vote (age ≥ 18).
# x = int(input("Please enter a age:"))
# if x >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# #1.Write a program to check whether a number is positive or negative.
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")
# #2.Check whether a number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# # 4.Compare two numbers and print the greater number.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if num1 > num2:
#     print("Greater number is:", num1)
# elif num2 > num1:
#     print("Greater number is:", num2)
# else:
#     print("Both numbers are equal")

# # 5.Check whether a given number is zero or not.
# num = int(input("Enter a number: "))
# if num == 0 :
#     print("The number is Zero")
# else :
#     print("The number is not Zero")

# #6.Check whether a year is a leap year or not.
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")

# #7.Take a number and print “Pass” if marks ≥ 40 else “Fail”.
# marks = float(input("Enter marks: "))
# if marks>=40 :
#     print("Pass")
# else :
#     print("Fail")

# #8.Check if a character is a vowel or consonant.
# char = input("Enter a character: ")
# if char.upper() in "AEIOU":
#     print("The character is a vowel.")
# else:
#     print("The character is a consonant.")

# #9.Check whether a number is divisible by 5.
# num = int(input("Enter a number: "))
# if num % 5 == 0 :
#     print("The number is divisible by 5 ")
# else :
#      print("The number is not divisible by 5 ")

# #10.Check whether a temperature is hot (>30) or normal.
# temp = int(input("Enter temperature: "))
# if temp >= 30 :
#     print("The temperature is hot . ")
# else :
#     print("The temperature is normal.")

# #11.Write a program to assign grades:≥90 → A  ≥75 → B  ≥60 → C Else → Fail.
# grade = float(input("Enter grade: "))
# if grade >=90:
#     print("Grade A")
# elif grade >=75:
#     print("Grade B")
# elif grade >=60:
#     print("Grade C")
# else:
#     print("Fail")

# #12.Check whether a number is: Positive  Negative  Zero
# num = float(input("Enter a number: "))
# if num >0 :
#     print("Positive number")
# elif num <0 :
#     print ("Negative number")
# else:
#     print("Zero")


# #13. Take age and decide: Child (0–12) Teen (13–19)Adult (20+)
# age = int(input("Enter age: "))
# if age<= 12:
#     print("Child")
# elif age <= 19:
#     print("Teen")
# else:
#     print("Adult")

#14.Build a simple calculator using if-elif-else (+, -, *, /).
# num1 = float(input("Enter first number: "))
# # num2 = float(input("Enter second number "))
# # operator = input("Enter operator (+, -, *, /): ")
# # if operator == "+":
# #     print("Result:", num1 + num2)
# # elif operator == "-":
# #     print("Result:", num1 - num2)
# # elif operator == "*":
# #     print("Result:",num1 * num2)
# # elif operator == "/":
# #     print("Result:",num1 / num2)

# #15.Check whether a triangle is: Equilateral  Isosceles Scalene
# side1 = float(input("Enter first side: "))
# side2 = float(input("Enter second side: "))
# side3 = float(input("Enter third side: "))
# if side1 == side2 == side3:
#     print("Equilateral triangle")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

#17.Print weekday name based on number (1–7)
# day = int(input("Enter a number (1-7): "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5: 
#     print("Friday")
# elif day == 6 :
#     print("Saturday")
# else:
#     print("Sunday")

#17.Check whether a number is 1-digit, 2-digit, or 3-digit.
# num = int(input("Enter a number :"))
# if num <10:
#     print("1-digit number")
# elif num<100:
#     print("2-digit number")
# elif num<1000:
#         print("3-digit number")
# else:
#      print("4-digit or more")

#18.Determine BMI category based on BMI value.
# bmi = float(input("Enter BMI: "))
# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi < 25:
#     print("Normal weight")
# elif 25 <= bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")
#19.Check whether a number is divisible by 3, 5, or both.
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by both 3 and 5")
# elif num % 3 == 0:
#     print("Divisible by 3")
# elif num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by either")

# #20.Electricity bill logic based on units consumed.
# units = int(input("Enter units consumed: ")) 
# if units <= 100:
#     print("₹5 per unit")
# elif units <= 200:
#     print("₹7 per unit")
# elif units < 300:
#     print("₹10 per unit")
# else:
#     print("₹15 per unit")

# #21.Check login: If username is correct Then check pass.
# username = input("Enter username: ")
# if username == "admin":
#     pass = input("Enter pass: ")
#     if pass == "pass":
#         print("Login successful.")
#     else:
#         print("Incorrect password.")
# else:
#     print("Incorrect username.")

#22.ATM withdrawal system: Check pin Check balance Deduct amount
# key = 1234
# balance = 10000

# entered = int(input("Enter your PIN: "))

# if entered == key:
#     withdraw_amount = int(input("Enter amount to withdraw: "))
    
#     if withdraw_amount <= balance:
#         balance = balance - withdraw_amount
#         print("Withdrawal successful")
#         print("Remaining balance:", balance)
#     else:
#         print("Insufficient balance")
# else:
#     print("Invalid PIN")

#26.Food ordering app:  Restaurant open/closed  Item available or not
# restaurant_status = input("Is the restaurant open? (yes/no): ")
# if restaurant_status == "yes":
#     item = input("Enter the item you want to order: ")
#     if item == "pizza":
#         print("Pizza is available.")
#     elif item == "burger":
#         print("Burger is available.")
#     elif item == "Panipuri":
#         print("Panipuri is available.")
#     else:
#         print("Item not available.")
# else:
#     print("Restaurant is closed.")

# #27.Online shopping discount system:    Cart value  Membership type
# card_value = float(input("Enter cart value: "))
# membership_type = input("Enter membership type (regular/premium): ")
# if card_value >= 1000 and membership_type == "premium":
#     print("20% discount applied.")
# elif card_value >= 1000 and membership_type == "regular":
#     print("5% discount applied.")
# elif card_value >= 500 and membership_type == "premium":
#     print("2% discount applied.")
# else:
#     print("No discount applied.")

# #28.Cab booking:    Distance    Time (day/night)
# distance = float(input("Enter distance:"))
# time = input("Enter time (day/night): ")
# if distance <= 5:
#     print("Cab booked for 50 rupees.")
# elif distance <=10:
#     print("Cab booked for 100 rupees.")
# else:
#     print("Cab booked for 200 rupees.")

