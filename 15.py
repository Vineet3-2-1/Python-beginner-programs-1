# Checking if the number is Positive, Negative or Zero

try:
    num = int(input("Enter the number here: "))

    if(num>=0):
        if(num==0):
            print("It is Zero")
        else:
            print("It is Positive")
        
    elif(num<0):
        print("It is Negative")

except Exception as k:
    print("Invalid input! Please enter number only")