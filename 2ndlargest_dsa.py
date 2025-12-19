arr=[70,2,40,50,1,90]
maximum=arr[0]
second_max=arr[0]
for i in range(1,len(arr)):
    if arr[i]>maximum:
        second_max=maximum # store old max
        maximum=arr[i]
    elif arr[i]>second_max and arr[i]!=maximum:
        second_max=arr[i]
print(second_max)
print(maximum)
