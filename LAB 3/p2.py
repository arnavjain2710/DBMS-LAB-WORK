# Q2 Write a Python program to perform arithmetical operations such as addition of two numbers, multiplication of two numbers, etc.
# Note: Input numbers should be taken from the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print("The sum of {} and {} is {}".format(num1, num2, addition))
print("The difference of {} and {} is {}".format(num1, num2, subtraction))
print("The product of {} and {} is {}".format(num1, num2, multiplication))
print("The quotient of {} and {} is {}".format(num1, num2, division))