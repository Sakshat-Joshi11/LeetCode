"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      if not head :
        return head
      else:  
        curr = head
        prev = None  
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev  
      return prev        