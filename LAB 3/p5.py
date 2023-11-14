# Q5 Write a Python program for finding nth Fibonacci number.

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the value of n: "))
print("The {} Fibonacci number is: {}".format(n , fibonacci(n)))