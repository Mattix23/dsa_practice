"""Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Summary:
In this problem, we are to arrange the numbers in a list in ascending order. If the list was 5,3,2,1 then the output we want is 1,2,3,4,5.

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Some test cases for these example can be the result should be true when the numbers are in ascending order.

Approach:
The approach to this problem is a divide and conquer approach. Based on todays lesson, we will use merge sort to return a list in ascending order. 
First we will keep splitting the list until we cannot split it any longer, ususally this means the list became individual elements. 
Then we merge the two individual elements into sorted order by comparing if one element is larger than another. 
In order to achieve this, we will create pointers to keep track of the separate values."""




def sortArray(nums: list[int]) -> list[int]:
    # function in charge of merging the lists
    def merge(arr, L, M, R):
        left = arr[L:M+1]
        right = arr[M+1:R+1]
        # i begins at the start of array, j and k are pointers at the beginning of the sub arrays created
        i = L
        j = 0
        k = 0
        # if both pointers are in bounds, compare and figure out which has a smaller value, then insert value into array.
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            # always increment i pointer regardless
            i += 1
        # if left sub array has values remaining, add values from that sub array
        while j < len(left):
            nums[i] = left[j]
            j+= 1
            i += 1
        # if right sub array has values remaining, add values from that sub array
        while j < len(right):
            nums[i] = right[k]
            k+= 1
            i += 1

    def mergeSort(arr, left, right):
        # if the size of the array is 1, returns the array
        if left == right:
            return arr
        # implements recursion, finds middle boundary in order to split array into two sides
        middle = (left + right) // 2
        mergeSort(arr, left, middle)
        mergeSort(arr, middle + 1, right)
        # merges the sub arrays and returns the sorted array
        merge(arr, left, middle, right)
        return arr

    return mergeSort(nums, 0, len(nums) - 1)