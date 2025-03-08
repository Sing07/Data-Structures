a1 = [1,3,5,9]
a2 = [2,6,4,8]
a3 = [5,3,234,2,46,457,34,52,2,6,3,7,6]
def merge(a1,a2):
    combined = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            combined.append(a1[i])
            i += 1
        else:
            combined.append(a2[j])
            j += 1
    
    while i < len(a1):
        combined.append(a1[i])
        i += 1
    while j < len(a2):
        combined.append(a2[j])
        j += 1
    
    return combined

# print(merge(a1,a2))
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid_index = len(arr)//2
    left = mergeSort(arr[:mid_index])
    right = mergeSort(arr[mid_index:])

    return merge(left, right)

print(mergeSort(a3))