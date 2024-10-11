word = input("Enter a string: ").lower()

while not word.isalpha ():
    print("Not a string. Enter a valid string!")
    word = input("Enter a string again: ").lower()

reversed_str = ''
for char in word:
        reversed_str = char + reversed_str

if reversed_str == word:
    print(f"{reversed_str} is a Palindrome!")
else:
     print(f"{reversed_str} is not a Palindrome!")



