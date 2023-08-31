arr0 = [1,7,4,2,1,3,11,5]
target0 = 10
output0 = 2,6

def subarray_sum(arr,target):
    pass


"""
1. generic array where subarray is in center
2. subarray is at the start
3. at the end
4. no sbarray
5. have 0 in list
6. multiple subarray with same sum
7. empty array
8. subarray is a single element
"""


# Brute Force approach
def subarray_sum1(arr,target):
    n = len(arr)
    # i goes from 0 to n-1
    for i in range(0,n):
        # j goes from i to n
        for j in range(i,n+1):
            #check if subarray sum eqal target
            if sum(arr[i:j]) == target:
                #answer found
                return i, j
    return None, None


# Better approach

def subarray_sum2(arr, target):
    n = len(arr)
    #i goes from 0 to n-1
    for i in range(0,n):
        s = 0
        for j in range(i,n+1):
            if s == target:
                return i,j
            elif s > target:
                break
            if j < n:
                s += arr[j]
    return None, None


# Optimal 
def subarray_sum3(arr, target):
    n = len(arr)
    i,j,s=0
    while i < n and j < n+1:
        if s == target:
            return i,j
        elif s < target:
            if j < n:
                s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None



