l=[10,"hello","meher",True]
for i in l:
    print(i,end="")
#how to access element of list
#list[index]
list=["html",'css',"js","java"]
i=0
while i>=0 and i<=3:
     print(list[i])
     i=i+1


a=len(list)
i=0
while(i<a):
    print(list[i])
    i=i+1
print("completed")


#list in built function
list.append("c++")
list.insert(2,"dsa")
print(list,len(list))
list.remove(2)
list.pop("java")
list.sort()
