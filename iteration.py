#for loop
#-----
#if we want to execute a group of statement for every element present in given collection(str,list,tuple,range)
#all elements of the collection me want to print.



str="ayush"
for x in str:
    print(str,end="")
    #end is used to new line konsa style ne hoga
#task1
num=input("enter the name")
for x in num:
    print(num,end="**")

#task2
i=0
for a in num:
    print(a  , "present in ", i,"index")
    i+=1
    
#list- if we want to store multiple value  in single  variable where order is required
#to preserved  and duplicate are allowed then we have to use list in python.

#a) list is denoted by square bracket[]
#b)duplicate values are allowed
#c)indexing is allowed
#d)different datatypes are allowed


#len
#len function is  used find the length of any collection(str, list,set,dict,tuple)// space is also include space
str="ram hello ayush whatups bro"
print(len(str))
#syntax of python list
#------------------------------
listName=[10,33.3,"list2","list3","list4"]
print(listName(3))

