# Q3 Write a Python program to swap two variables.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
temp = a
a = b
b = temp
print("a = {} b = {}".format(a, b))