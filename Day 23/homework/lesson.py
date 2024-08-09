#davaleba 1



# num = int(input("Enter number from 1 to 100: "))

# while True:
#     my_guess = int(input("My guess: " ))
#     if num == my_guess:
#         print("Correct")
#         break
#     else:
#         print("try again")


#davaleba 2

# for i in range(101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     else:
#         print(i)


#daveleba 3

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

#davaleba 4

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