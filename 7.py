# Find the area of triangle

a = int(input("Enter the first side here: "))
b = int(input("Enter the second side here: "))
c = int(input("Enter the third side here: "))

#We will use Heron's formula as all three sides are known

#1. Calculate the semi-perimeter
sp = (a+b+c)/2

#2. Now using Heron's formula
ans = (sp*(sp-a)*(sp-b)*(sp-c))**(1/2)

print(f"Area of Triangle = {ans}")