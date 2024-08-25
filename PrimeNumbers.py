# Function to check if a given number is prime
def prime_checker(number):
  # Assume the number is prime until proven otherwise
  is_prime = True

  # Check divisibility from 2 to number-1
  for i in range(2,number):
    if number % i == 0:
      # If the number is divisible by any i, it's not a prime
      is_prime = False 

  # Print the result based on the is_prime flag
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.") 

n = int(input("Give me a number: "))  

# Call the prime_checker function with the user-provided number
prime_checker(number=n)