a=input("enter your class")
b=int(input("enter your attendence"))
c=int(input("enter one if there is any medical"))
if(b>=75):
  print("you are allowed")
elif(b<75):
  if c==1:
    print("you are allowed")
else:
      print("you are not allowed")
