input_str = "teeter"

for char in input_str:
    print("Current character:", char)
    if input_str.count(char) == 1:
        print("The first non-repeated character is:", char)
        break
    else:
        print("No non-repeated character found.")
        break