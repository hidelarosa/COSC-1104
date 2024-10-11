temperature = (input("Please enter your temperature: "))
while not temperature.isnumeric():
    print("Not a number. Please enter a valid number")
    temperature = (input("Please enter a number: "))

if int(temperature) > 30:
    print("You are hot!")
else:
     print ("You are cold!")