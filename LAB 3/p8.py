# Q8 Take input (integer) from the user and check if input is a prime number or not.

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

n = int(input("Enter a number: "))
is_prime_number = is_prime(n)
if is_prime_number:
   print(n, "is a prime number")
else:
   print(n, "is not a prime number")