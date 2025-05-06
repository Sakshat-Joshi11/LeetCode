"""
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

    For example, the following two linked lists begin to intersect at node c1:
    
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        tempA,tempB = headA, headB
        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA
    
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
s = Solution()
print(s.getIntersectionNode(listA,listB)) 