# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(-1)
        head=dummy
        
        while l1 or l2:
            
            if not l2:
                head.next=ListNode((l1.val+carry)%10)
                carry=(l1.val+carry)//10
                head=head.next
                l1=l1.next
            elif not l1:
                head.next=ListNode((l2.val+carry)%10)
                carry=(l2.val+carry)//10
                head=head.next
                l2=l2.next
            else:
                summ=l1.val+l2.val+carry
                head.next=ListNode(summ%10)
                carry=summ//10
                head=head.next
                l1=l1.next
                l2=l2.next
            if carry:
                head.next=ListNode(1)
        return dummy.next
        