print ("Hello World!")

#this is a comment

'''
this is a line of comments
line 2
line 3
'''

# line 1 - to do this for mutliple lines hit command /
# line 2
# line 3

# Variables
x = 10 # in python you dont decalre a variable type, you just declare teh variable and asign it a value
x = "hello"
x = [1,2,3]

x = 100
y = 10
result = x // y #when doing division in python, the result is always a float, so to make it an int, do a double //
print(result)

x = 10.5
x = int(x)
print(x)

min_val = min(10,1)
print(min_val)

max_val = max(10,1)
print(max_val)

raised = pow(2,4) #OR
raised = 2**4
print(raised)

#if statements in python
if x<10:
    print("less")
    x = 11
    x += 1

print("continue")

if x<10 and y>100:
    print("do something")

if x<10 or y>100:
    print("do something else")


if x<10:
    print("less")
elif x>10 and x<15:
    print("middle")
else:
    print("other")

# for loops

nums = [10,20,30,40,50]

for i in range(1, len(nums)-1):
    print(nums[i])

for val in nums:
    print(val)

for i, val in enumerate(nums):
    print(i, val)

dogs = ["Rocky", "Boomer", "Daisy"]
nums2 = [1,2,3,4,5]

for i in range(len(dogs)):
    print(dogs[i])

for dog in dogs:
    print(dog)

for i, dog in enumerate(dogs):
    print(i, dog)

total = 0
for i in range (len(nums2)):
    total += nums2[i]
    
print(total)

# Functions (like methods in Java)

def hello_world():
    count = 0
    while count < 5:
        print("Hello World!")
        count += 1

hello_world()

def hello(name):
    print("Hello " + name)

hello("Claire")

def hello2(name="friend"): #giving this a default value
    print("Hello " + name)

hello2() #WITHOUT INPUT
hello2("Claire") #WITH INPUT

first_name = "Claire"
last_name = "Gaza"
full_name = first_name + " " + last_name
print(full_name) 

print(full_name.upper())

first_initial = full_name[0]
last_name_initial = full_name[7]

print("First name inital: " + first_initial)
print("Last name inital: " + last_name_initial)
print("last character in name: " + full_name[-1]) # you can use negative numbers to get characters at the end of a string

python_repeate3 = "Python" * 3
print(python_repeate3)

magician = "Harry Houdini"
if magician == "Harry Houdini":
    print("World's Greatest Magician!")

# Slicing (allows us to slice a string or list of elements at a given index place)
# new_String = String[start_index : end_index+1]

platform_computing = "Platform Computing"
platform = platform_computing[0:8]
computing = platform_computing[9:]
print(platform)
print(computing)

# Activity

nums = [0,3,4,5,8]

temp = nums[1]
nums[1] = nums[3]
nums[3] = temp

print(nums)




