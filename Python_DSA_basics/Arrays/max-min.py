def minmax(arr):
    if not arr:
        return None
    
    max = arr[0]
    for element in arr:
        if element > max:
            max = element
    return max

arr = [1,2,124,53,21,24,5,2,2,2,32,4]

maxvalue = minmax(arr)

print("max value in array is", maxvalue)
