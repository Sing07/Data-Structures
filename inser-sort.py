arr = [29, 10, 14,37, 15]

# def inserSort(arr):
#     for i in range(1, len(arr)):
#         inner = i
#         while arr[inner - 1] > arr[inner] and inner > 0:
#             arr[inner - 1], arr[inner] = arr[inner], arr[inner-1]
#             inner -= 1
        


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j- 1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

insertionSort(arr)
print(arr)


print(arr[:])
print(arr[3:])
print(arr[4:])
