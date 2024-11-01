# In-Class 4: Main Program
# Date: November 1, 2024
# Authors: Harlan Dela Rosa & Angela Reyes
 
import json
 
def retrieve_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
 
def filter_instances(instances, min_vcpu, max_vcpu, min_memory, max_memory): 

    filtered_instances = []
   
    for instance in instances:
        vcpu = int(instance['vcpu'].split()[0])  # Get the first integer from vCPU string
        memory = float(instance['memory'].split()[0])  # Get the first float from memory string
       
        if (vcpu >= min_vcpu and (max_vcpu is None or vcpu <= max_vcpu) and
            memory >= min_memory and (max_memory is None or memory <= max_memory)):
            filtered_instances.append(instance)
   
    return filtered_instances
 
def display_ec2_instances(instances):
    """Display the filtered EC2 instances."""
    if not instances:
        print("No EC2 instances meet your requirements.")
        return
   
    print("\nMatching EC2 Instances:")
    for instance in instances:
        print(f"Name: {instance['name']}, vCPU: {instance['vcpu']}, Memory: {instance['memory']}, Storage: {instance['storage']}, Bandwidth: {instance['bandwidth']}, Availability: {instance['availability']}")
 
if __name__ == '__main__':
    file_path = 'ec2_instance_types.json'  # Path of the JSON file. Should matched with JSON filename.
    # User Inputs
    while True:
        try:
            min_vcpu = int(input("Enter the minimum required CPU cores: "))
            max_vcpu = input("Enter the maximum required CPU cores (press Enter for no limit): ")
            max_vcpu = int(max_vcpu) if max_vcpu else None
            break
        except ValueError:
            print("Please enter valid integers for CPU cores.")
 
    while True:
        try:
            min_memory = float(input("Enter the minimum required memory in GiB : "))
            max_memory = input("Enter the maximum required memory in GiB (press Enter for no limit): ")
            max_memory = float(max_memory) if max_memory else None
            break
        except ValueError:
            print("Please enter valid numbers for memory.")
   
    instances = retrieve_data(file_path)
    filtered_instances = filter_instances(instances, min_vcpu, max_vcpu, min_memory, max_memory)
    display_ec2_instances(filtered_instances)
 