#  Basics in Python Dictionary

# chai_types = {"Masala chai":"spicy","Ginger chai":"gingery", "Cardamom chai":"cardamomy"}
# print(chai_types)

# print(chai_types["Masala chai"])
# print(chai_types.get("Ginger chai"))
# chai_types["Ginger chai"] = "green"
# print(chai_types)

# for chai in chai_types:
#     print(chai_types[chai])


# #  Iteration over dictionary items

# for key ,value in chai_types.items():
#     print(f"{key} is {value}")


# #  Conditional statement in dictionary

# if("Masala chai" in chai_types):
#     print("Masala chai hai")

# chai_types["Lemon chai"]= "Lemony"
# print(chai_types)

# print(len(chai_types))

# chai_types.pop("Lemon chai")
# print(chai_types)

# chai_types.popitem()
# print(chai_types)




squared_numbers ={x:x**2 for x in range(1,11)}
print(squared_numbers)

squared_numbers.clear()
print(squared_numbers)

key = ["Masla chai", "Ginger chai", "Cardamom chai"]
print(key)

default_value = "Spicy"
key_value_pair = dict.fromkeys(key,default_value)
print(key_value_pair)