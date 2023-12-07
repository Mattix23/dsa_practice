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

class Node:
    def __init__(self, data):
        # create the node object
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # create the head of the linked list
        self.head = None
        self.size = 0

        # function to add new node at the beginning of the list
    def insertFirst(self, new_data):   
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode
        else:
            # link this node to the previous head with the next property
            newNode.next = self.head
            # set this node as the new head
            self.head = newNode
        self.size += 1

    def removeFirst(self):
        if self.head:
            oldHead = self.head
            newHead = oldHead.next
            self.head = newHead
            self.size -=1
            return oldHead
    
    def getFirst(self):
        return self.head
    
    def getSize(self):
        return self.size

    def reverse(self):
        node = self.head
        previous = None
        temp = None
        while node:
            # store next pointer before overwriting
            temp = node.next
            # reverse the pointer
            node.next = previous
            
            # move forward
            previous = node
            node = temp
        # set the final node to be the new head
        self.head = previous
 
        # helper function to print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

llist = LinkedList()
llist.insertFirst(20)
llist.insertFirst(4)
llist.insertFirst(15)
llist.insertFirst(85)
 
print ("Given linked list")
llist.printList()
# prints 85, 15, 4, 20
llist.reverse()
print ("\nReversed linked list")
llist.printList()
# prints 20, 4, 15, 85