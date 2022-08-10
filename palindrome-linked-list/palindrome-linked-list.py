# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        ''' reverse the linked list as we go till middle then one pointer travel from 
            middle to head and another one from middle to end'''
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            '''reverse'''
            nextt=slow.next
            slow.next=prev
            prev=slow
            slow=nextt
        if fast:  #if fast still present is odd number of nodes case
            slow = slow.next
        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
        return not prev