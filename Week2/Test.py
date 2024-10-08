
# Function to calculate Grades
def calculate_avg(grades):

    total = sum(grades)
    avg = total/len(grades)
    return avg

# Function to define letter grade
def get_letter_grade(avg):
    if (avg >= 90):
        return 'A'
    elif (avg >=80):
        return 'B'
    elif (avg >=70):
        return 'C'
    elif (avg >=60):
        return 'D'
    else:
        return 'E'

# Main Method
if __name__ == "__main__":
    num_subjects = int(input(f'Please Enter Number of Subjects {i + 1}: '))
    grades_list = []

# Loop to interate through the number of subjects
    for i in range(num_subjects):
        grade = float(input("Enter Your Grade:"))
        grades_list.append(grade)

# Calculate the average
avg = calculate_avg(grades_list)

# Get the letter grade
letter_grade = get_letter_grade(avg)

# Display the results

print(f'The average grade is :{ avg }')
print(f' the letter grade is :{ letter_grade}')