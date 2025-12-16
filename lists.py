#creation
numbers=[10,20,30,40]
names=["ADITI","RAJ","SAM"]

#access
print(numbers[0])
print(names[1])

#update
numbers[2]=35
names.append("Alex")

#looping
for num in numbers :
    print(num)

#custom examples
squares=[]
for i in range (1,6):
    squares.append(i*i)
print(squares)

even_numbers=[n for n in numbers if n%2==0]
print(even_numbers)

total=0
for n in numbers:
    total+=n
print(total)
