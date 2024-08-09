
#1) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ორი რიცხვი და შემდეგ დაბეჭდოს მათი ჯამი.

num1 = float(input('Please Enter Your Number: '))
num2 = float(input('Please Enter Your Number: '))

sum = num1 + num2
print("The sum off",  num1, "and", num2, "is", sum)


#2)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის ფართობს. პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.

width = float(input("enter the width of the rectangle: "))
height = float(input("enter the height of the rectangle: "))

area = width * height

print("the area of the rectangle with width", width, "and height", height, "is: ", area)

#3) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს ამ რიცხვის ორმაგი.

number = float(input("enter a number: "))
double = number * 2
print("double of", number, "Is: ", double)

#4)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის პერიმეტრს. პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.

width = float(input("Enter The Width Of The Rectangle: "))
height = float(input("Enter The Height Of Rectangle: "))
perimeter = 2 * (width + height)
print("The Perimeter Of The Rectangle With Width", width, "And Height", height, "Is: ", perimeter)

#5) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს ამ რიცხვის კვადრატი(გამოიყენეთ ** - ოპერატორი)

number = float(input("Enter A Number: "))
square = number ** 2 
print("Square Of", number, "Is: ", square)