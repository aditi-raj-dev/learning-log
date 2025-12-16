#1. reverse a list(no slicing)
nums=[1,2,3,4,5]
reversed_list=[]
for i in range(len(nums)-1,-1,-1):
    reversed_list.append(nums[i])
print(reversed_list)

#2. count frequency of elements
items=[1,2,2,3,3,3] 
freq={}
for item in items:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)

#3. remove duplicates preserving order
data=[1,2,2,3,1,4]
result=[]
seen=set()
for x in data:
    if x not in seen:
        result.append(x)
        seen.add(x)
print(result)

#4. find max and min without built-ins
numbers=[4,7,1,9,3]
max_value= numbers[0]
min_value= numbers[0]

for n in numbers:
    if n>max_value:
        max_value=n
    if n< min_value:
        min_value=n

print("max",max_value)
print("min",min_value)

#5. word frequency in a string
text="python is easy and python is poweful"
words = text.split()
word_freq={}

for word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1

print(word_freq)