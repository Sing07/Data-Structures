arr1 = [1,4,5,8,9]
arr2 = [2,3,6,7]

arr = [23,76,3,2,34,6,5,4,2,34,1,5,56]

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(l1, l2):
    combined = []
    i = 0
    j = 0
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[j])
            j += 1

    while i < len(l1):
        combined.append(l1[i])
        i += 1
    while j < len(l2):
        combined.append(l2[j])
        j += 1
    return combined

print(merge(arr1, arr2))

print(merge_sort(arr))


