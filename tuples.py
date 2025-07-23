#tuples
ayu=("ayu",True,233,233,22.9)
a=()#empty tuples
print(type(ayu))
i=0
while i<=4:
 print(ayu[i])
 i += 1
  
print("*"*20)
# count and len and index are in inbuilt methods
b=print(len(ayu))
i=0
while(i<5):
    print(ayu[i], " present at ",i,"index")
    i+=1


print("*"*20)

#range
r=range(4,22,2)
for a in r:
    print(a, end="\t")
print("out of loop")