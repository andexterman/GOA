
# while True:
#     age = int(input("Enter your age: "))
#     experience = int(input("How many years of driving experience do you have?: "))
#     if age > 0 and experience > 0:
#         if age < 18:
#             print("You aren't old enough to have a driving license")
#         elif age >= 18 and experience >= 1:
#             print("You can have a driving license")
#         elif age >=18 and experience < 1:
#             print("You don't have enough experience to have a driving license ")
#         break
#     else:
#         print("Please enter valid number ")

# while True:
#     mid_term = int(input("Enter your mid-term exam grade: "))
#     final = int(input("Enter your final exam grade: "))
#     project = int(input("Enter your project grade: "))
#     if 0 < mid_term <= 100 or 0 < final <= 100 and 0 < project <= 100:
#         if mid_term + final + project >= 70:
#             print("You passed")
#         else:
#             print("You failed")
#         break
#     else:
#         print("Please enter valid grade (Greater than 0)")
    
# while True:
#     mid_term = int(input("Enter your mid term exam grade: "))
#     final = int(input("Enter you final exam grade: "))
#     project = int(input("Enter your project grade: "))
#     if 0 < mid_term <= 100 and 0 < final <= 100 and 0 < project <= 100:
#         average = (mid_term + final + project) / 3
#         if average >= 70:
#             print("You passed")
#         else:
#             print('You failed')
#         break
#     else:
#         print("Please enter valid grade")