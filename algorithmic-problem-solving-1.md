Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

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

Summary:
The problem is asking to find a single integer in an array, where the array includes integers that can appear more than once. The output of this problem is the integer that appears once.

Example:
Input/Outputs of this problem would include something like [1,1,2,3,3] where the desired integer on this input would be "2" since that is the only integer to appear once. Some edge cases in this can be an empty list, where it should return false or None since the result is intended to be an integer.
Another example can be a list where all numbers appear once, or all numbers appear multiple times. [1,2,3] or [1,1,2,2,3,3] in this case, the first output should return all the list, since each one is shown once and the second list would return none.
