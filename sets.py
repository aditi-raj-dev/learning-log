#creation 
nums={1,2,3,4}
letters=set(["a","b","c"])

#add and remove
nums.add(5)
nums.remove(2)

#looping 
for n in nums:
    print(n)

#custom examples
values=[1,2,2,3,4,4]
unique_values=set(values)
print(unique_values)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

print(3 in set1)