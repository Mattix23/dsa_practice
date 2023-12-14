"""
Find the node with minimum value in a Binary Search Tree.

Summary: The task for this problem is to find the value to the most left of the tree, as this value will be the minimum value.

Example 1:
Input = [22,12,30,8,20]
Output = 8

Approach:
The approach to this problem is to construct a BST, traverse the tree with the divide and conquer approach by creating nodes and pointers.
After dividing, we will then continue to the most left of the tree, where we will find the minimum value.
"""


class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def insert(node, new_data):
 
    # 1. If the tree is empty, return a new node
    if node is None:
        newNode = Node(new_data)
        return newNode
    else:
        # 2. Otherwise, go down the tree
        if new_data <= node.data:
            node.left = insert(node.left, new_data)
        else:
            node.right = insert(node.right, new_data)
 
        # Return the (unchanged) node pointer
        return node
 
 
def min_value(node):
    current = node
 
    # loop down to find the leftmost node
    while(current.left is not None):
        current = current.left
 
    return current.data
 
 

# Testing
root = None
root = insert(root, 4)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 6)
insert(root, 5)

# Function call
print(f"The minimum value is {min_value(root)}")