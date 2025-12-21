## problem 1: move all zeros to end (in place)
def move_zero(arr):
    pos=0  # position to place next non zero
    for i in range (len(arr)):# to fill non zero elements at starting 
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos+=1
    for i in range (pos,len(arr)):# to fill remaining spaces by 0
        arr[i]=0
    
    print(arr)
arr=[1,0,3,0,6,7,0,9]
move_zero(arr)


## problem 2: intersection of two arrays 
def intersection(arr1,arr2):
    freq={}
    result=[]
    for i in arr1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for num in arr2:
        if num in freq and freq[num]>0:
            result.append(num)
            freq[num]-=1
    print (result)

arr1=[1,2,3,4,5,2,1]
arr2=[2,3,4,2,2,1,3,5,7]
intersection(arr1,arr2)


## problem 3: Majority element(>n/2 times)
def majority_element(arr3):
    candidate=None
    count=0
    for num in arr3:
        if count==0: #  different elements cancel each other majority remains
            candidate=num
            count=1
        elif num==candidate:
            count+=1
        else:
            count-=1
    print (candidate)

arr3=[2,3,4,5,3,4,5,3,3,3,3,3,3]
majority_element(arr3)


## problem 4 : Check if two strings are anagrams
# anagrams have same no of letters same no of frequency of appearing characters 
def is_anagram(s1,s2):
    anagram=True
    if len(s1)!=len(s2):
        print("NOT ANAGRAMS")
    
    count={}
    #count character in s1
    for ch in s1:
        count[ch]=count.get(ch,0)+1

    # reduce using s2
    for ch in s2:
        if  ch not in count or count[ch]==0:
            anagram=False
            if not anagram:
                print("NOT ANAGRAM")
        count[ch]-=1
    if anagram:
        print("Yes anagram")

s1="listen"
s2="silent"
is_anagram(s1,s2)

