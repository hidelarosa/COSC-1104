'''
Week 2 Exercises - Variables, Conditions, Loops
Author: Harlan Dela Rosa
Class: COSC1104
'''

# Exercise 1 - Vowel Counter
# Skills: Variables, String Manipulation, Loops, Conditions

# Take user input for a random string
user_string = input ("Enter a random string: ").lower()

# List of vowels

vowels = ['a','e','i','o','u']

# Count the vowels
vowel_counter = [0,0,0,0,0]

#iterate through each character in the user input

for each_char in user_string:
    if each_char in vowels:
        # Find the index of the vowel located in the list
        index = vowels.index(each_char)
        # Increment the counter located in vowel_counter
        vowel_counter[index] += 1

# Display the counter for each vowel
for i in range(len(vowels)):
    print(f'{vowels[i]} - {vowel_counter[i]}')


# Exercise 2 - Sum of Digits
# Skills: Variables, Type Casting, Loops, Conditions
user_input = input 



