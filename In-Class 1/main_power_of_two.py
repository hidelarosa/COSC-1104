from PowerOfTwo import *

if __name__ == "__main__":
    input_num = 2  
    input_num1 = 4
    input_num2 = 6
    input_num3 = 1024

    checker = PowerOfTwo() 
    result = checker.is_power_of_two(input_num) 
    result1 = checker.is_power_of_two(input_num1) 
    print(f"{input_num} is a power of two: {result}")
    print(f"{input_num1} is a power of two: {result1}")