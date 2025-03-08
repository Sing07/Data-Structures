from typing import List


# def display_coordinates(x, y):
#     print(f"X: {x}, Y: {y}")

# coordinates = (10, 20)
# display_coordinates(*coordinates)


# list1 = [2,3,4]
# list2 = [5,1,7]

# def item_in_common(list1, list2):
#     my_dict = {}
#     for i in list1:
#         my_dict[i] = 0

#     for j in list2:
#         if j in my_dict:
#             return True
    
#     return False

# print(item_in_common(list1, list2))


############################################################


# def first_non_repeating_char(string):
#     for index, c in enumerate(string):
#         if string[index] != string[index+1]:
#             return string[index]
#         if index > 1:
#             return None
#     return None


# print( first_non_repeating_char('leetcode') )

# print( first_non_repeating_char('hello') )

# print( first_non_repeating_char('aabbcc') )


# list = {}

# arr = [5, 1, 7, 2, 9, 3]

# # for i, elem in enumerate(arr):
# #     list[i] = elem

# print(list)

# for i in arr:
#     list[i] = i

# print(list)

############################################################

# def find_pairs(a1, a2, target):
#     for i in a1[::-1]:
#         print(i)
        

# arr1 = [1, 2, 3, 4, 5]
# find_pairs(arr1)

############################################################

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# def longest(nums):
#     max_sum = nums[0]  # Initialize max_sum to the first element of the array
#     cur_sum = nums[0]  # Initialize cur_sum to the first element of the array

#     for num in nums[1:]:  # Start from the second element
#         cur_sum = max(num, cur_sum + num)  # Update cur_sum with the maximum of current number and (cur_sum + num)
#         max_sum = max(max_sum, cur_sum)  # Update max_sum if cur_sum is greater

#     return max_sum

# def longest(nums):
#     max_sum = nums[0]
#     maxone = 0

#     for num in nums:
#         max_sum = max(num, max_sum + num)
#         maxone = max(max_sum, maxone)
#         print("max_sum:", max_sum, "\n")


#     return maxone

# print(longest(arr))

# print(max(-2,1))

############################################################
# arr = [1,2,3,4,5]

# for i in range(0,len(arr)):
#     print(i)

# s = "Was it a car or a cat I saw?"

# print(s)

# news = "".join(char for char in s if char.isalnum()).lower()
# # wasitacaroracatisaw
# print(news)

# # output:
# # 0
# # 1
# # 2
# # 3
# # 4

############################################################

# nums = [-1,0,1,2,-1,-4]
# final = []

# print(sorted(nums))
# # [-4, -1, -1, 0, 1, 2]
# s_nums = sorted(nums)

# for i, n in enumerate(s_nums):
#     # Skip duplicate elements
#     if i > 0 and s_nums[i] == s_nums[i - 1]:
#         continue
    
#     l, r = i + 1, len(s_nums) - 1

#     while l < r:
#         if n + s_nums[l] + s_nums[r] < 0:
#             l += 1
#         elif n + s_nums[l] + s_nums[r] > 0:
#             r -= 1
#         else:
#             final.append([n, s_nums[l], s_nums[r]])
#             # Skip duplicate elements
#             while l < r and s_nums[l] == s_nums[l + 1]:
#                 l += 1
#             while l < r and s_nums[r] == s_nums[r - 1]:
#                 r -= 1
#             l += 1
#             r -= 1

# print(final)



############################################################

# print(ord('x')) # 120 
# print(ord('y')) # 121
# print(ord('z')) # 122


# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     # Initialize output array with 1s
#     output = [1] * n
#     left_products = [1] * n
#     right_products = [1] * n
    
#     for i in range(0, n-1):
#         left_products[i] = left_products[i] * left_products[i+1]

#     print(left_products)

# # Test the function
# nums = [1, 2, 4, 6]
# (productExceptSelf(nums))  # Output: [48, 24, 12, 8]

############################################################

# a = [4,9,3,2]
# b = [7,5,8,93,1]

a = [1,2,3,4,6]
b = [5,7,8,9,10]

def merge(a,b):
    i = 0
    j = 0
    arr = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr.append(a[i])
            i +=1
        elif a[i] > b[j]:
            arr.append(b[j])
            j +=1

    while i < len(a):
        arr.append(a[i])
        i +=1
    while j < len(b):
        arr.append(b[j])
        j +=1
    return arr

print(merge(a,b))