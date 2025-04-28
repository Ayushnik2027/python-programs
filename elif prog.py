marks=int(input("enter the number:"))
if(marks<40):
    print("you are fail:")
elif(marks<50 and marks>40):
    print("you are pass")
elif(marks<100 and marks>90):
    print("you are topper")
else:
    print("you are just pass")
