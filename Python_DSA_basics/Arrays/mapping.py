#Using map() Function:
def map_array(arr, transformation):
    return list(map(transformation, arr))

# Example usage:
my_array = [1, 2, 3, 4, 5]

# Square each element
mapped_array = map_array(my_array, lambda x: x ** 2)

print("Original Array:", my_array)
print("Mapped Array (Square each element):", mapped_array)

#Using List Comprehension:
def map_array_with_list_comprehension(arr, transformation):
    return [transformation(x) for x in arr]

# Example usage:
my_array = [1, 2, 3, 4, 5]

# Double each element
mapped_array = map_array_with_list_comprehension(my_array, lambda x: x * 2)

print("Original Array:", my_array)
print("Mapped Array (Double each element):", mapped_array)
