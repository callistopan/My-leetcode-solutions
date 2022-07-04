# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return head
        if head.next==None:
            return head
        odd=head
        even=head.next
        t=even
        while even and even.next:
            odd.next=even.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=t
        return head
    
    
    def even_odd_merge(self,head):
        
        '''using dummy node'''
        
        if not head:
            return head

        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)

        tails,turn = [even_dummy,odd_dummy],0

        while head:

            tails[turn].next = head

            head = head.next

            tails[turn] = tails[turn].next

            turn ^= 1 # we use XOR to flip the turn

        tails[1].next = None
        tails[0].next = odd_dummy.next

        return even_dummy.next
        
            
        
        