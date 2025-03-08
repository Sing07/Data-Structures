arr = [6, 3, 23, 7, 45, 36, 1]


def binsearch(arr, target):
    if not arr:  # Base case: if the array is empty
        return False
    
    mid = len(arr)//2
    if target == arr[mid]:
        return mid  # Return the index of the target value
    elif target < arr[mid]:
        return binsearch(arr[:mid], target)
    elif target > arr[mid]:
        result = binsearch(arr[mid+1:], target)
        if result is not False:
            return mid + 1 + result  # Adjust the index for the right half of the array
        else:
            return False
    else:
        return False

def binSearch(arr, target):
    high = len(arr) - 1
    low = 0
    
    while low <= high:
        # mid = (high - low) //2
        mid = (high + low) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target :
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

ar2 = [1, 2, 3 ,4, 5, 6, 7, 8, 10, 11, 12]

print(binSearch(ar2,11))

