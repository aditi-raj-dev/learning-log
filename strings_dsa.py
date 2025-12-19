#reverse a string without using slicing

s=input("enter string=")
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)


##palindrome check 
is_palindrome=True
left=0
right=len(s)-1
for i in range (len(s)):
    if s[left]!=s[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
print(is_palindrome)


##character frequency
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)

## first non repeating character 
si="swiss"
fre={}
for ch in si:
    if ch in fre:
        fre[ch]+=1
    else:
        fre[ch]=1
for i in si:
    if fre[i]==1:
        print("first non repeating character is:",i)
        break

