items = ["apple", "banana","orange","apple"]

unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate found: {item}")
    else:
        unique_items.add(item)