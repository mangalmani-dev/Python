
#  some basics of the list data types in python
tea_varieties = ["black","green","white","oolong","herbal"]
# print(tea_varieties)
# print(tea_varieties[1:4])
# print(tea_varieties[2:])
# tea_varieties[1]= "Lemon tea"
# print(tea_varieties)
# tea_varieties[1:2]= "green"
# print(tea_varieties)

# tea_varieties[1:2]= ["Ginger"]
# print(tea_varieties)

# tea_varieties[1:3] = ["Kela , Laung"]
# print(tea_varieties)

# print(tea_varieties)
# tea_varieties[1:1] = ["test","test"]
# print(tea_varieties) 

#  concept of slicing and replacing the elements in the list
# tea_varieties[1:2]=["test1","test2"]
# print(tea_varieties)
# print(tea_varieties[1:3])
# tea_varieties[1:3]=[]
# print(tea_varieties)


# print(tea_varieties)

# Looping throgh list
# for tea in tea_varieties:
#     print(tea)

# for tea in tea_varieties:
#      print(tea,end="-")

# #  Conditional statement with list
# tea_varieties.append("Lemon tea")

# if "Lemon tea" in tea_varieties:
#     print("Lemon tea is available")

# print(tea_varieties)
# tea_varieties.pop()
# print(tea_varieties)
# tea_varieties.remove("oolong")
# print(tea_varieties) 

# tea_varieties.insert(1,"Kala tea")
# print(tea_varieties)

#  concept of deep copy and shallow copy
# print(tea_varieties)
# tea_varieties_copy = tea_varieties.copy()
# print(tea_varieties_copy)
# tea_varieties_copy.append("Milk tea")
# print(tea_varieties_copy)
# print(tea_varieties)


#  squared numbers using list

print(range(1,10))
squared_numbers = [x**2 for x in range(1,11)]
print(squared_numbers)

