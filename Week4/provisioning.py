# COSC 1104 - In-Class 1-Part 1  
# GROUP 7 - Dela Rosa, Harlan & Reyes, Angela Jonyl
# 09/27/2024

# Declaration of constants
# Total Resource Capacity 
TOTAL_CPU_CORES = 16
TOTAL_MEMORY_GB = 64

# User Input
USER_INPUT_CPU = input("Please enter the amount of CPU: ")
USER_INPUT_MEM = input("Please enter the amount of MEM: ")

# Check if the inputs are digits
if not USER_INPUT_CPU.isdigit() or not USER_INPUT_MEM.isdigit():
    print("Invalid input: Characters are not allowed. Please enter valid integers.")
else:
    # Convert inputs to integers
    USER_INPUT_CPU = int(USER_INPUT_CPU)
    USER_INPUT_MEM = int(USER_INPUT_MEM)

    # Check for negative values
    if USER_INPUT_CPU < 0 or USER_INPUT_MEM < 0:
        print("Negative values are not allowed")

    # Check for over capacity
    elif USER_INPUT_CPU > TOTAL_CPU_CORES or USER_INPUT_MEM > TOTAL_MEMORY_GB:
        print("User input is over the available capacity")

    else:
        REMAINING_CPU_CORES = TOTAL_CPU_CORES - USER_INPUT_CPU
        REMAINING_MEM_GB = TOTAL_MEMORY_GB - USER_INPUT_MEM

        print(f'The remaining available CPU cores: {REMAINING_CPU_CORES}')
        print(f'The remaining available MEMORY (GB): {REMAINING_MEM_GB}')