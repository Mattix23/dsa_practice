"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

def find_single_num(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
        # If the number exists, increments the counter by 1 for that number
            num_count[num] += 1
        else:
        # if the number doesn't exist, add the number and set the counter of that number to 1
            num_count[num] = 1
    for num, count in num_count.items():
        # iterate through the dictionary searching for the number that has the value as 1 and return it
        if count == 1:
            return num
        
# arr = [2,2,1]
# arr = [3,3,4,5,5,6,6]
# print(find_single_num(arr))