arr=[2,5,8,1,9]
is_sorted=True
for i in range (len(arr)):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)
