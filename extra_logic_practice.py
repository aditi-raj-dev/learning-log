# problem 1: Find missing number
def missing_number(nums):
    n=len(nums)
    total=n*(n+1)//2
    actual_sum=sum(nums)
    print("Required number=", total-actual_sum)

nums=[0,1,2,3,4,5,7,8,9,10]
missing_number(nums)


##Element appearing once (others twice)
def single_num(nums):
    result=0 # staring with 0 does not affect the answer
    for num in nums: # expand to result= result^num  # process every number exactly ones
        result^=num #XOR cancels duplicates 
        #x^x=0, x^0=x
    print("number appearing only once is :", result)

nums=[1,2,3,2,3]
single_num(nums)
