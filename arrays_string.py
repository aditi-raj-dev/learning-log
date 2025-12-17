#reverse string 
text="python"
reversed_text =""
for ch in text:
    reversed_text= ch+ reversed_text
print(reversed_text)

#check palindrome
word="madam"
is_palindrome=True

for i in range (len(word)//2):
    if word[i]!= word[len(word)-1-i]:
        is_palindrome=False
        break
print("palindrome:", is_palindrome)

#find duplicate characters 
string ="programming"
duplicates= set()

for i in range (len(string)):
    for j in range (i+1,len(string)):
        if string[i]==string[j]:
            duplicates.add(string[i])

print("duplicates:",duplicates)


#count vowels
sentence="learning python is fun"
vowels="aeiou"
count=0

for ch in sentence:
    if ch in vowels:
        count+=1

print("vowel count:", count)
