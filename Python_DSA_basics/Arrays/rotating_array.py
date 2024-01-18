def right_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # To handle cases where k is greater than the array length
    rotated_array = arr[-k:] + arr[:-k]
    return rotated_array

my_array = [1, 2, 3, 4, 5]
k_right = 2

# Right rotating the array by k positions
rotated_array_right = right_rotate_array(my_array, k_right)

print("Original array:", my_array)
print(f"Right rotated array by {k_right} positions:", rotated_array_right)
