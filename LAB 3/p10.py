# Q10 Write a Python program to find minimum and maximum value in a list.

def find_min_max(list):
  min_value = list[0]
  max_value = list[0]
  for value in list:
    if value < min_value:
      min_value = value
    if value > max_value:
      max_value = value
  return (min_value, max_value)

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    list.append(element)

min_value, max_value = find_min_max(list)
print("The minimum value is:", min_value)
print("The maximum value is:", max_value)