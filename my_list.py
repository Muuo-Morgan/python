# Empty list
my_list = []

# Append elements 14, 24, 34, 44, 54
my_list.append(14)
my_list.append(24)
my_list.append(34)
my_list.append(44)
my_list.append(54)

# Insert value 15 at the second position
my_list.insert(1, 15)

# Extend with [52, 62, 74]
my_list.extend([52, 62, 74])

# Remove the last element
my_list.pop(7)

# Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 34
index_of_34 = my_list.index(34)
print("List:", my_list)
print("Index of 34:", index_of_34)
