# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        ref=head
        while n>0:   # two pointer approach
            ref=ref.next
            n-=1
        if ref is None:#no further elements    (if we want to delete the firs element in the list)
            return head.next
        else:#we have to traverse further(size(linked list )-n) time
            main=head
            while ref.next:
                main=main.next
                ref=ref.next
            main.next=main.next.next
        return head
        