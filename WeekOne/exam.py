# COSC 1104 - In-Class 1-Part 2
# GROUP 7 - Dela Rosa, Harlan & Reyes, Angela Jonyl
# 09/27/2024
# Description: Allocates CPU cores and memory, and tracks pending requests .
# Declarations
# Constants representing the total capacity.
TOTAL_CPU_CORES = 16
TOTAL_MEMORY_GB = 64.0
 
# Variables for the remaining capacity; to be reduced as things are allocated.
remaining_cpu_cores = TOTAL_CPU_CORES
remaining_memory_gb = TOTAL_MEMORY_GB
 
# Empty lists for tracking resources.
allocated_resources = list()
pending_requests = list()
 
# The loop will continue as long as this variable is equal to “yes”.
# At the end of the loop, ask the user if they want to continue.
is_continuing = "yes"  # Use double quotes instead of curly quotes
 
while is_continuing.lower() == "yes":
    u = input("Username: ")
    # Directly accepting CPU cores and memory input
    cpu = input("CPU cores: ")  
    mem = input("Memory (GB): ")
 
    if not cpu.isdigit() or not mem.isdigit():
        print("CPU input: Please enter valid integers.")
    else:
    # Convert inputs to integers
        cpu = int(cpu)
        mem = float(mem)
    # Check if resources are available
        if remaining_cpu_cores >= cpu and remaining_memory_gb >= mem:
            allocated_resources.append([u, cpu, mem])
            remaining_cpu_cores -= cpu
            remaining_memory_gb -= mem
        else:
            pending_requests.append([u, cpu, mem])
 
    # Ask if the user wants to continue
    is_continuing = input("Another request? (yes/no): ")
 
# Display Allocated Resources
print("\nAllocated Resources:")
for resource in allocated_resources:
    print(f"User: {resource[0]}\tCPU cores: {resource[1]}\tMemory (GB): {resource[2]}")
 
# Display Pending Requests
print("\nPending Requests:")
for request in pending_requests:
    print(f"User: {request[0]}\tCPU cores: {request[1]}\tMemory (GB): {request[2]}")