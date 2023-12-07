"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Summary:
When a list is given such as  [1,2,3,4,5], the result or return value should be [5,4,3,2,1]

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Approach:
The approach to this problem will include creating pointers to keep track of the list in its given state [1,2,3,4,5] and another pointer to keep track of the reversed order.
We will use a node object to be the element in the list and alter this node.

A common test for this problem would look like 
result = [1,2,3,4,5]
self.assertEquals(result, [5,4,3,2,1])

"""