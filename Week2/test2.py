# Define a function to create a dog with a name
def create_dog(name):
    return {"name": name}

# Define a function for the dog to bark
def bark(dog):
    print(f"{dog['name']} is barking!")

# Creating dogs (dictionaries) with names
dog = create_dog("Buddy")
bark(dog)  # Calling the bark function with the 'my_dog' dictionary

dog = create_dog("Peanut")
bark(dog)  # Calling the bark function with the 'my_dog1' dictionary
