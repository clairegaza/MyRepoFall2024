# name = input("Enter your name: ")
# print(name)

# try:
#     num = int(input("Enter a number: "))
#     num += 1
#     print(num)
# except:
#     print("Enter a number")

for i in range(5):
    print(i, end=" ") #this will print all the numbers on the same line
print()

name = "Jim"
age = 14
print(f"{name}, in {18-age} years you can vote.")

with open("movies.txt") as file:
    for line in file:
        line = line.strip()
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        info = line.split()
        info[2] = int(info[2])
        fname, lname, height = line.split() #this you can only do if you know how your lines are going to be split / how many variables you have
        print(info)
        print(fname, lname, height)