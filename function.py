#Function definition
def greet():
    print("hello! welcome.")

greet()

#parameters vs arguments 
def greet_user(name):
    print("hello",name)

greet_user("ADITI")

#Return values
def add(a,b):
    return a+b

result = add(4,6)
print("sum",result)

#default parameters
def power(base, exp=2):
    return base ** exp
print(power(5))
print(power(2,3))

#custom functions( 5 small tasks)
def is_even(num):
    return num%2==0

def find_square(num):
    return num*num

def count_character(text):
    return len(text)

def maximum(a,b,c):
    max_val=a
    if b>max_val:
        max_val=b
    if c>max_val:
        max_val=c
    return max_val

def reverse_string (text):
    reversed_text=""
    for ch in text :
        reversed_text= ch+ reversed_text
    return reversed_text

print(is_even(4))
print(find_square(6))
print(count_character("python"))
print(maximum(3,5,7))
print(reverse_string("coding"))

