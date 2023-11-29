
a=int(input("Enter days"))
b=int(input("enter month"))
c=int(input("enter year"))

if (a>30):
 print("invalade date:a")
 
 if (b>12):
  print("invalade month:b")

 if (c>99):
  print("invalde year:c")
 if (b==2):
  if (c%4==0):
    print("")
  elif(a>29):
   print("invalade date")

print(a,"/",b,"/",c)
