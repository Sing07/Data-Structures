a = [5,9,12,56]
b = [7,8,45,51]
c = [5,9,12,56,7,8,45,51]

# def mergeSort(c):

#     if len(a) > 1:
#         left_arr = c[:len(c)//2]
#         right_arr = c[len(c)//2:]

#         mergeSort(left_arr)
#         mergeSort(right_arr)

#         merge(left_arr,right_arr)

# def merge(a,b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)

#     i = j = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         elif a[i] > b[j]:
#             sorted_list.append(b[j])
#             j += 1
        
#     return sorted_list    


# mergeSort(c)
# # print(merge(a,b))
 


arr = [0, 2, 4, 6, 8, None, None, None]  # Initialized with extra space for merging
left_arr = [1, 3, 5]  # Sorted array
right_arr = [7, 9]    # Sorted array
nn = []
temp_arr = arr[:]  # Create a copy of arr
temp_arr.extend(left_arr)  # Extend the copy with left_arr
nn = temp_arr  # Assign the extended list to nn



print(nn)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]