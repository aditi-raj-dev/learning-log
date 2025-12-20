##HASHING 

#Frequency of elements using dictionary
arr=[10,20,10,20,30,20,40,50,10]
freq={}
for num in  (arr): # traverse arra's each element
    if num in freq: #check if each element exists in freq dictionary
        freq[num]+=1 #increase count
    else:
        freq[num]=1 #add first time
print(freq)

#First repeating element
seen={}
for i in arr:
    if i in seen:
        print("first repeating element=",i)
        break
    else:
        seen[i]=1

#Two sum problem
arr1=[2,9,11,7,22]
dic1={}
target=11
for j in  (arr1): # traversing each element
    needed=target-j # to get needed element
    if needed in dic1:# check if that element is present in made dictionary
        print("required pair ", j,"and",needed)
        break
    else:
        dic1[j]=1
