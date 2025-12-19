#to reverse array in place that is no new array 
#two pointers 
arr=[10,20,30,40,50]
start =0
end=len(arr)-1
while start<end :
    arr[start],arr[end]= arr[end],arr[start] # swap start and end 
    start+=1 # move inward
    end-=1
print(arr)