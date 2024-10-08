# COSC 1104 – Assignment 1
# Harlan Dela Rosa

# Option 1: Create an application that will analyze whether a number is a prime number or not and provide some additional information around it.

def user_input():
    x = input("Please enter a number: ")
    
    while not x.isnumeric():  # Check if input is a valid positive integer
        print("Not a valid positive whole number. Please enter a valid positive whole number.")
        x = input("Please enter a number: ")
        
    return int(x)

def is_prime(number): # Check if the input number is prime
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisibility up to the square root of n
        if number % i == 0:
            return False # Return false if number is not primary to print the number is not prime
    return True # Return true if number is primary to print the number is prime
        
def is_next_prime(number): # find the next prime number
    number = number + 1
    while True: 
        if is_prime(number): # check if the next number is prime
            return number
        number = number + 1 

def is_before_prime(number): # find the prime number before the input number
    number = number - 1
    while True:
        if is_prime(number): # check if the next number is prime
            return number
        number = number - 1


# Get user input
number = user_input()

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")   
    
else:
    def factors(number):
        l = []
        for i in range(1, number+1):
                if number % i == 0:
                    l += [i]
        return l
    list = factors(number)
    print(f"{number} is not a prime number. The list of factors is: {list}")

next_prime = is_next_prime(number)
if is_next_prime(number):
    print(f"{next_prime} is the next prime number of {number}. ")

before_prime = is_before_prime(number)
if is_before_prime(number):
    print(f"{before_prime} is the prime number before {number}. ") 


