arr = [12, 5, 7, 32, 53, 2, 6]


def BubSort(arr):
    for i in range(len(arr)-1, 0 ,-1):
        for j in range(i):
            if arr[j] > arr[j +1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(BubSort(arr))