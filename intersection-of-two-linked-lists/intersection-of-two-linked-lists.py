# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        ''' if the linked lists are given such that they do not intersect then the loop will end if both of them are none as none==none
        if they intersect at any point then the travel distance ie.
        x+y+z=z+y+x so they intersect at a node and continue united :)'''
        
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
            
        return a if a else None