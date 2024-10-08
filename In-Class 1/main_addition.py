from AddNumbers import *

if __name__ == "__main__":
    add_numbers = AddNumbers()  # Create an instance of AddNumbers
    result = add_numbers.sum_of_digits(123)
    result1 = add_numbers.sum_of_digits(10.15)  # Call the method and store the result
    result2 = add_numbers.sum_of_digits(11111) 
    print(f"The sum of digits is: {result}")
    print(f"The sum of digits is: {result1}")
    print(f"The sum of digits is: {result2}")