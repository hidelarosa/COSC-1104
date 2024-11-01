def ave_grades(subject_grades):
    ave = int(sum(int(grade) for grade in subject_grades.values()) / len(subject_grades))
    return ave


if __name__ == "__main__":
    student = input("Enter your name: ")
    student_id = input("Enter your student number: ")

    subject_grades = {}
    while True:
        subject = input("Enter the subject: Type 'end' when you're finished! ")
        if subject.lower() == 'end':
            break
        grade = input("Enter your grade: ")
        subject_grades[subject] = grade

    print("\nStudent Grades Report:")
    print(f"Name: {student}")
    print(f"Student ID: {student_id}\n")
    
    for subject, grade in subject_grades.items():
        print(f"  {subject}: {grade}")

    # Calculate average
    if subject_grades:
        average = ave_grades(subject_grades)
        print(f"\nAverage Grade: {average}")
    else:
        print("\nNo grades entered.")