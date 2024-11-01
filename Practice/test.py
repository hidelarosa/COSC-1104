memory = []
users = []
total_memory = 60

user = input("Enter your name: ")

while user.isnumeric():
    print("Invalid input. Please enter your name again:")
    user = input("Enter your name: ")

while True:
    user_input = input("Enter the amount of memory you need: (type 'end' when done or 'new' for new requestor): ")
    while not user_input.isnumeric() and user_input != 'end' and user_input != 'new':
        print("Invalid input. Please enter the value again:")
        user_input = input("Enter the amount of memory you need: (type 'end' or 'new' for new requestor): ")
    if user_input == 'end':
        break
    if user_input == 'new':
        user = input("Enter your name: ")
        while user.isnumeric():
            print("Invalid input. Please enter your name again:")
            user_input = input("Enter your name: ")
        continue

    memory.append(int(user_input))

remaining_memory = total_memory - sum(memory)
total_mem_requested = sum(memory)
print(f"The name of the requestor is: {user}")
if sum(memory) > total_memory:
    print(f"Memory requested is {total_mem_requested} exceeds the limit by {remaining_memory*(-1)}")
else:
    print(f"Memory requested is {total_mem_requested}.")
    print(f"Remaining memory left is: {remaining_memory}")