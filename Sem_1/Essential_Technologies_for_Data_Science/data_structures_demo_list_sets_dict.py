# List
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
print("First fruit:", fruits[0])

# Add an item
fruits.append("orange")
print("After adding:", fruits)

# Update an item
fruits[1] = "blueberry"
print("After updating:", fruits)

# Remove an item
fruits.remove("apple")
print("After removing:", fruits)

print()  # Line break

# Set
numbers = {1, 2, 3, 2, 1}
print("Original Set:", numbers)

# Add an item
numbers.add(4)
print("After adding:", numbers)

# Update (sets don’t have indexes, so we can only add/remove)
numbers.update({5, 6})
print("After updating with multiple values:", numbers)

# Remove an item
numbers.remove(2)
print("After removing:", numbers)

print()  # Line break

# Dictionary
person = {"name": "Alice", "age": 25}
print("Original Dictionary:", person)
print("Person's name:", person["name"])

# Add a new key-value pair
person["city"] = "New York"
print("After adding:", person)

# Update a value
person["age"] = 26
print("After updating:", person)

# Remove a key-value pair
person.pop("name")
print("After removing:", person)
