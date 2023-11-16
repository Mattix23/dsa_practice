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

Approach:
The solution/approach we came up with was to create a loop that iterates through the array to compare the elements. But unsure how to code this out exactly.
something like 
"for element in array:
    if the element is equal to the current index return the current element"
this would iterate through the array, if the numbers are the same then that would return that integer, otherwise it keeps iterating until it finds one. The issue with this comes down to the length of the list. If the list is too long, then this will take a long time.
Another approach would be to initiate a counter using a dictionary to keep track of the values, and then add that number to the dictionary. If the number is not in the dictionary then we add it with a count of 1 (this is for tracking purposes), if it is in the dictionary then we increment the current number by 1.
num_dict = {}
    loop here through the array
    if the num in the array is in the dictionary, add it with a counter of 1
    else add the number with the count as 1
a for loop through the dictionary to find the "1" counter
return the number that has that counter"


