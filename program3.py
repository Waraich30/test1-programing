x=input("Enter coumtry name:")
y=int(input("Salary:"))

if (x=="canada"):
    salary=y*1.49
    if (y>56000):
        print("you will rich")
    else: 
        print("you will poor")

elif (x=="USA"):
    salary=y*1.10
    if (y>45000):
        print("you will rich")
    else: 
        print("you will poor")

elif (x=="cambodia"):
    salary=y*4000
    if (y>7649856):
        print("you will rich")
    else: 
        print("you will poor")

elif (x=="uk"):
    salary=y*.86
    if (y>45423):
        print("you will rich")
    else: 
        print("you will poor")
