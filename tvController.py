from pult import *

print("""----Pult Menu----
1. TV Power ON/Off
2. TV Info
3. Channels Amount
4. Add Channel
5. Random Channel
6. Change Volume

`-1` -> EXIT,bro!""")

p1 = Pult()

while True:
    bottom = input("Enter Bottom: ")
    if(bottom == '-1'):
        print("Controller ended!")
        break
    if(bottom == '1'):
        p1.tv_power()
    elif(bottom == '2'):
        print(p1)
    elif(bottom == '3'):
        print("Channel Amount: ",len(p1),"ta")
    elif(bottom == '4'):
        p1.add_channel(input("Channel Name: "))
    elif(bottom == '5'):
        p1.random_channel()
    elif(bottom == '6'):
        p1.volumeUp_Down()
    else:
        print("Bro, enter 1-7 numbers, please!")
