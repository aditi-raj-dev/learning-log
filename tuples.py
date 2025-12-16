#creation
point=(10,20)
colors=("red","green","blue")

#access
print(point[0])
print(colors[2])

#looping
for color in colors:
    print(color)

#custom examples
dimension=(1920,1080)
print("width",dimension[0])
print("height",dimension[1])


marks=[85,90,78]
total=0
for m in marks:
    total+=m
print(total)

single_value=(5,)
print(type(single_value))
