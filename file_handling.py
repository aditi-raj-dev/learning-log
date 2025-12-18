# writing to a file
with open ("data.txt","w") as file:
    file.write("learning file handling in python\n")
    file.write("this is DAY 4 \n")

# reading from a file
with open ("data.txt","r") as file:
    context=file.read()
    print(context)

# appending to a file 
with open ("data.txt","a") as file:
    file.write("appending new line \n")

#handling file not found error
try:
    with open ("unkown.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found. please check the filename.")
