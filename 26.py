# factorial program

def funn(num):
    if num==0:
        return 1
    return num * funn(num-1)

num = int(input("Enter the number here: "))
fac = funn(num)
print(f"The factorial of {num} = {fac}")