# LINEAR SEARCH

arr1=[10,20,30,40,50]
target=30
found=False
for i in range (len(arr1)): # traversing whole array
    if arr1[i]==target:
        found=True
        print("Element found at index:",i) # in this case it should print index 2
if not found:
    print("element not found")


# BINARY SEARCH
low=0
high=len(arr1)-1
target1=40
found1=False
while low<=high:
    mid=(low+high)//2
    if arr1[mid]==target1:
        print("target is found at index:",mid)
        found1=True
        break
    elif arr1[mid]>target1:
        high=mid-1  # search left half
    elif arr1[mid]<target1:
        low=mid+1  # search right half
if not found1:
    print("target not found")


#  BUBBLE SORT 
arr=[27,38,46,59,1,30]
n=len(arr)
for i in range (0,n):# loop should run n no of times because each time only 1 elemnt is sorted
    for j in range (n-i-1):# i elemnts are sorted in n elemnts and 1 element is j+1 element
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# SELECTION SORT
for k in range (0,n): # n no of times because each loop fixes 1 position
    min_index=k
    for l in range (i+1,n): # i elemnts are already sorted before hand 
        if arr[l]<arr[min_index]:
            min_index=l
    arr[k],arr[min_index]=arr[min_index],arr[k]
print(arr)
