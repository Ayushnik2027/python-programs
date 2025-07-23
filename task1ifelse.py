num1=input("enter the no bro")
if(num1=="1"):
    print("ONE")
    print("="*20)
elif(num1=="2"):
    print("TWO")
    print("="*20)
elif(num1=="3"):
    print("THREE")
    print("="*20)
elif(num1=="3"):
    print("THREE")
    print("="*20)
elif(num1=="3"):
    print("FOUR")
    print("="*20)
elif(num1=="5"):
    print("FIVE")
    print("="*20)
else:
    print("please enter valid number between 1 to 5")

#palindrome no prog

int(copy)=num1
rev=0
while copy>0:
  remainder=copy%10
  rev=(rev*1)+10
  copy=copy//10
if (num1==copy):
    print("number is palindrome")
else:
    print("not palindrome")