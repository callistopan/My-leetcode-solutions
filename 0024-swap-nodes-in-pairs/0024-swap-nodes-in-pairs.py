# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        new_start = head.next.next
        head,head.next=head.next,head
        head.next.next = self.swapPairs(new_start)
        return head
    
    def swapPairs_iterative(self,head):
        prev=dummy=ListNode(None)
        
        while head and head.next:
            next_head=head.next.next
            prev.next=head.next
            head.next.next=head
            prev=head
            head=next_head
            
        prev.next=head
        return dummy.next
        