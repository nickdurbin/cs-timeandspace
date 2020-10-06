"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""

# O(n^2) time and O(1) space
def remove_duplicates(nums):
    for x in nums: # O(n)
        i = nums[x+1]
        if nums[x + 1] == i: # O(n) 
            nums.pop(i)
    return nums

nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))

# O(n) both space and complexity
# def remove_duplicates(nums):
#     num_set = set(nums)
#     return list(nums)

# O(n) time and O(1) space
# def remove_duplicates(nums):
#     non_dups = 0
#     for i in range(1, len(nums)):
#         if nums[i] == nums[non_dups - 1]:
#             continue
#         else:
#             nums[non_dups] = nums[i]
#             non_dups += 1
#     return nums, non_dups