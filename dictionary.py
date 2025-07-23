
d={"ayush":"tiwari","college name": "lu", "age": 21}

#to add a data
d["father name"]="gopi tiwari"
#to delete the data
del d["age"]
#empty dictionary
D={}


#break
for i in range(0,10):
    if i==6:
        break
    print(i,end="\t")

#num1=int(input("enter the values"))
#l=[10,20,0,5,7,6,1]
#for i in l:
  #   val=num1//i
  #   if(i==0):
  #     break
   #  print(val)
#print("good")
    
#continues
for x in range(5):
    if x==3:
        continue
    print(x)
    
t=[10,20,30,40,500,60,300,600]
for x in t:
    if x>=500:
        continue
    print(x)
for x in t:
    if x>=500:
        break
    print(x)