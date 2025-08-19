#Swapping two numbers

a = int(input("Enter the first number here: "))
b = int(input("Enter the second number here: "))

print(f"The numbers before swapping are {a} and {b}")

temp = a
a = b
b = temp

print(f"The values after swapping = {a} and {b}")
