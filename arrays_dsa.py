#to print largest and smallest from  a array
arr=[10,3,7,9,20]
largest=arr[0]
smallest=arr[0]
for i in range (1,len(arr)):  # this loop travesrses each element of array and comapare it to get largest and smallest value possible 
    if arr[i]>largest:
        largest=arr[i]
    if arr[i]<smallest:
        smallest=arr[i]
print(largest)
print(smallest)
