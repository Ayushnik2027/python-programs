num1=float(input("enter your number"))
num2=float(input("enter your 2 number"))
op=input("enter the operator")
if(op=="+"):
    res=num1+num2
    print("="*20)
    print("the sum is :",res)
    print("="*20)
elif(op=="-"):
    res=num1-num2
    print("="*20)
    print("the subsraction is :",res)
    print("="*20)
elif(op=="/"):
    res=num1/num2
    print("="*20)
    print("the division is :",res)
    print("="*20)
elif(op=="//"):
    res=num1//num2
    print("="*20)
    print("the floor division is :",res)
    print("="*20)
elif(op=="*"):
    res=num1*num2
    print("="*20)
    print("the multiplication is :",res)
    print("="*20)
elif(op=="**"):
    res=num1-num2
    print("="**20)
    print("the exponent power is :",res)
    print("="*20)
else:
    print("please enter the valid operator")
