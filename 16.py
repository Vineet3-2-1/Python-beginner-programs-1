# Convert seconds to hours, minutes and seconds

sec = int(input("Enter Second here: "))
s = sec
m, h = 0,0
if(s>60):
    m = s // 60
    s = s % 60

    if(m>60):
     h = m // 60
     m = m % 60
                
     print(f"Hour = {h}\nMinute = {m}\nSecond = {s}")

    else:
       print(f"Hour = {h}\nMinute = {m}\nSecond = {s}")
                

else:
    print(f"Second = {sec}")