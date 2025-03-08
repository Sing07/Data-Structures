
arr = [54, 21, 4, 68, 2, 6, 9, 25]
arr2 = [99,88,77,66,55,44,33,22,11,1]

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


BubbleSort(arr2)
