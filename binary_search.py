# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

"""
Summary:
For this problem, we are to asked to find a specific target in the array of integers. When that targer is found, we return the index it is located in, if it is not found then we return -1

Example:
Some examples of this problem would include a list of integers [1,2,3,4,5,6], if the target number is 4, then we would return 3 because that is the index of the target. 
If the target is not found then we would return -1"

Approach:
For this solution, we decided to use a binary search as that is suggested for this problem. We would create two pointers to traverse the list, and another variable that would locate the middle of the list. 
If that number in the middle is greater than one of the pointers we subtract 1 from the mid number, otherwise we add 1 to one of the pointers. 
If either is not located, then we can assume that mid value is the target and we return that, otherwise we return -1. 
"""

# Solution

def search_for_num(nums: list[int], target:int) -> int:
    p1 = 0
    p2 = len(nums)-1
    while p1 <= p2:
        middle_pointer = p1 + (p2-p1) // 2
        if nums[middle_pointer] > target:
            p2 = middle_pointer - 1
        elif nums[middle_pointer] < target:
            p1 = middle_pointer + 1
        else:
            return middle_pointer
    return -1