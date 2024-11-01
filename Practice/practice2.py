os_list = list()
while True:
    x = (input("Enter number: "))
    if not x.isnumeric() and x != 'end':
        print("Invalid number. Please enter again. ")
        continue
    if x == 'end':
        break
    os_list.append(int(x))
    total = sum((os_list))
    ave = total/(len(os_list))
print(f"The sum of all input is: {total}")
print(f"The average is: {ave}")


