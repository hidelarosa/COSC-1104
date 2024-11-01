memory = []
users = []
total_memory = 60

user = input("Enter your name: ")

# Check if name is valid
while user.isnumeric():
    print("Invalid input. Please enter your name again:")
    user = input("Enter your name: ")

while True:
    user_input = input("Enter the amount of memory you need (type 'end' when done, 'new' for a new requestor): ")

    # Validate the user input
    while not user_input.isnumeric() and user_input != 'end' and user_input != 'new':
        print("Invalid input. Please enter the value again:")
        user_input = input("Enter the amount of memory you need (type 'end' or 'new' for a new requestor): ")

    if user_input == 'end':
        break
    if user_input == 'new':
        user = input("Enter your name: ")
        while user.isnumeric():
            print("Invalid input. Please enter your name again:")
            user = input("Enter your name: ")
        continue
    
    memory_request = int(user_input)
    memory.append((user, memory_request))  # Store memory requests along with user name
    users.append(user)  # Store the requestor

# Calculate remaining memory
used_memory = sum(memory_request for _, memory_request in memory)
remaining_memory = total_memory - used_memory

print(f"The name of the requestor is: {user}")
if used_memory > total_memory:
    print(f"Memory requested is {used_memory} and exceeds the limit of {total_memory}.")
else:
    print(f"Memory requested is {used_memory}.")
    print(f"Remaining memory left is: {remaining_memory}")