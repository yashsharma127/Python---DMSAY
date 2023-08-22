def search(nums1,nums2):
    n1,n2=len(nums1),len(nums2)
    n= n1 + n2

    ind2 = n//2
    ind1 = ind2 - 1
    cnt=0
    elem1,elem2=-1,-1
    i,j=0,0

    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if cnt == ind1:
                elem1 = nums1[i]
            if cnt == ind2:
                elem2 = nums1[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                elem1 = nums2[j]
            if cnt == ind2:
                elem2 = nums2[j]
            cnt += 1
            j += 1
    while i < n1:
        if cnt == ind1:
            elem1 = nums1[i]
        if cnt == ind2:
            elem2 = nums1[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            elem1 = nums2[j]
        if cnt == ind2:
            elem2 = nums2[j]
        cnt += 1
        j += 1

    if n % 2 ==1:
        return float(elem2)
    
    return float(elem1 + elem2) /2.0


nums1 = [1,3] 
nums2 = [2]

result = search(nums1,nums2)
print(result)