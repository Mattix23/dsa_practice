Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

# Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#### Test case:
def test_twoSum_example1():
    nums = [2, 7, 11, 15]
    target = 9
    expected_output = [0, 1]

    actual_output = twoSum(nums, target)

    assert expected_output == actual_output, "Expected output {} does not match actual output {}".format(expected_output, actual_output)

This test case defines a function `test_twoSum_example1()` that tests the behavior of the `twoSum` function for the provided example inputs. It first creates the input array `nums` and the target value `target`. Then, it calls the `twoSum` function with these inputs and stores the result in the variable `actual_output`. Finally, it asserts that the `actual_output` is equal to the expected output `expected_output`.


# Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

### Test Case :


# Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
 #### Test Case
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

# Sunmmary of problem, `big-O-1`:
Theres a list of numbers and a target number. You need to find two numbers in the list that add up to the target number.




# Psuedocode plan:


# Solution:
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
