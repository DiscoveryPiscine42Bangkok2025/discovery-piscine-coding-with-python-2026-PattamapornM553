first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
ans = first_number * second_number
print(f"{ans}")

if ans > 0:
    print("The result is positive.")
elif ans < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")