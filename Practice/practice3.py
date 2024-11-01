fruits = ["apple", "banana", "cherry"]
counter = 0

# while loop will run while counter is less than 5
while counter < 5:
    for fruit in fruits:
        print(f"I like {fruit}")
        fruits.append("1")
        counter += 1
        if counter >= 5:  # Stop when the counter reaches 5
            break