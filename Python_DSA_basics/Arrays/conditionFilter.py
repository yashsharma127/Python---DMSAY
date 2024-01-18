####
#Using filter() Function:
def filter_array(arr, condition):
    return list(filter(condition, arr))

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter elements greater than 5
filtered_array = filter_array(my_array, lambda x: x > 5)

print("Original Array:", my_array)
print("Filtered Array (Elements > 5):", filtered_array)

#######
# Using List Comprehension:
def filter_array_with_list_comprehension(arr, condition):
    return [x for x in arr if condition(x)]

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter elements less than or equal to 3
filtered_array = filter_array_with_list_comprehension(my_array, lambda x: x <= 3)

print("Original Array:", my_array)
print("Filtered Array (Elements <= 3):", filtered_array)
