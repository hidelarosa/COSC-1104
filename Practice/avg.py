def user_input():
    x = input("Please enter a number: ")
    
    while not x.isnumeric():  # Check if input is a valid positive integer
        print("Not a valid positive whole number. Please enter a valid positive whole number.")
        x = input("Please enter a number: ")
        
    return int(x)

def get_grades(number):
    grades = []
    while True:
        number = input("Enter grade (or 'end' to stop): ")
        if number.lower() == 'end':
            break
        else:
            grades.append(float(number))
        print(f"Grades entered: {grades}")


number = user_input()

