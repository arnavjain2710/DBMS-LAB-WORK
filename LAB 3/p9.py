# Q9 Write a Python program to convert string to lowercase.

def convert_to_lowercase(string):
  lowercase_string = string.lower()
  return lowercase_string

string = input("Enter a string: ")
lowercase_string = convert_to_lowercase(string)
print("The lowercased string is:", lowercase_string)