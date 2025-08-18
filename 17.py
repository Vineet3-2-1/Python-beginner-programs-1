# Checking divisibility of the numbers

num = int(input("Enter the number here: "))

if(num%5==0 and num%11==0):
    print(f"{num} is Divisible by both")

else:
    print(f"Either {num} is not divisble by one of these numbers or both")
