"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode , list2: ListNode ):
        dummy = ListNode()
        current = dummy
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next   

# Helper function to convert a Python list to a linked list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list (for display purposes)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Input two lists
list1_values = list(map(int, input("Enter the numbers for the list1 (comma-separated): ").split(",")))
list2_values = list(map(int, input("Enter the numbers for the list2 (comma-separated): ").split(",")))

# Convert Python lists to linked lists
list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

# Merge the lists
s = Solution()
merged_head = s.mergeTwoLists(list1, list2)

# Convert the merged linked list back to a Python list for display
merged_list = linked_list_to_list(merged_head)
print("Merged List:", merged_list)