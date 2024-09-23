numbers = input("Enter three numbers separated by spaces: ").split()

num1, num2, num3 = map(int, numbers)

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest number.")  # Using f-string for formatting
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest number.")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the greatest number.")
else:
    print("There was an error with your values.")

if num1 < num2 and num1 < num3:
    print(f"{num1} is the lowest number.")  # Using f-string for formatting
elif num2 < num1 and num2 < num3:
    print(f"{num2} is the lowest number.")
elif num3 < num1 and num3 < num2:
    print(f"{num3} is the lowest number.")
else:
    print("There was an error with your values.")
