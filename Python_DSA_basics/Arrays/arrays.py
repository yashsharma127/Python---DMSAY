my_array = [1, 2, 3, 4, 5]

# Inserting an element at a specific index
my_array.insert(2, 10)  # Insert the value 10 at index 2

print(my_array)


my_array = [1, 2, 3, 4, 5]

# Inserting an element at a specific index using slicing
index_to_insert = 2
value_to_insert = 10

my_array = my_array[:index_to_insert] + [value_to_insert] + my_array[index_to_insert:]

print(my_array)
