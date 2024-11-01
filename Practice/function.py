def calculate_avg(grades):
    total = sum(grades)
    avg = total / len(grades)
    return avg

# Function to determine the letter grade based on the average grade passed in
def get_letter_grade(avg):
    if (avg >= 90):
        return 'A'
    elif (avg >= 80):
        return 'B'
    elif (avg >= 70):
        return 'C'
    elif (avg >= 60):
        return 'D'
    else:
        return 'F'
    
# Main Method
if __name__ == "__main__":
    # Accept input for number of subjects
    num_subjects = int(input(f'Please Enter Number Of Subjects: '))
    grades_list = [] # Empty list of grades
    
    # Loop to iterate through the number of subjects
    for i in range(num_subjects):
        # Get Grade and append to grades_list
        grade = float(input(f'Enter Grade { i + 1 }: '))
        grades_list.append(grade)
    
    # Calculate the average grade
    avg = calculate_avg(grades_list)
    
    # Get the letter grade of the average
    letter_grade = get_letter_grade(avg)
    
    # Display the results
    print(f"The average grade is: { avg }")
    print(f'The letter grade is: { letter_grade }')