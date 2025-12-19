#to rotate k time from left
k=int(input("enter no of time to rotate:"))
arr=[10,20,30,40,50,60,70] 
n=len(arr)
for i in range(0,k): # k no of times is written so loop runs k-1 time because 1 elemnt is already stored and removed
    temp=arr[0] # store first element
    for j in range (0,n-1): # shift left upto 2 nd last place element
        arr[j]=arr[j+1]
    arr[n-1]=temp
print(arr)
