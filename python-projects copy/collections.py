lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

sliced_lst = lst[1:4]
print(sliced_lst)

lst.append(20)
lst.append(20)
print(lst)
num20 = lst.count(20)
print(num20)

copy = lst[:]
copy = lst.copy()
copy = lst
copy.append("new element")
print(copy)
print(lst)

empty = [0] * 10 #creates a list of size 10 with every element being 0
empty[5] = 15
print(empty)

empty = []
lst.remove("new element")
print(lst)

for val in lst:
    if val >= 20 and val <=40:
        empty.append(val)
print(empty)

#same as above just in a different way
new_lst = [val for val in lst if val>=20 and val<=40]
print("new lsit", new_lst)

nums = [x*x for x in range(1,10) if (x*x) % 2 == 0]
print(nums)

# Sets (like a list but it can't contain duplicates) THIS COULD COME IN HANDY WITH HOMEWORK 2
aset = {1,2,3} #uses curly brackets 
# x = aset[1] THIS DOESNT WORK BECUASE THE ORDER THAT ELEMENTS ARE STORED IN A SET ARE NOT GUARENTEED
dups = [1,1,1,2,2,2,3,4,4,4,5]
no_dups = set(dups) #this makes the list into a set
print(no_dups)

# Dictionary (what we called a hashmap in Java)
fav_foods = {"Kathleen" : "pizza", "Darien" : "sushi", "Roger" : "rice", "Lily" : "watermelon"} 
print(fav_foods)

kff = fav_foods["Kathleen"] #finding the value associated with teh key "kathleen"

for key in fav_foods:
    print(key, fav_foods[key])

for key, value in fav_foods.items():
    print(key, value)

if "Bob" in fav_foods:
    print("Bob's fav food is " + fav_foods["Bob"])
else:
    fav_foods["Bob"] = "cake"
print(fav_foods)

# dict = {}
# dict = dict()
