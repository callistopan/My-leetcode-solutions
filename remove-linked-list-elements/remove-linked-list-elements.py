# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, current = None, head
        while current:
            if current.val == val:
                if prev:
                    # Remove the current node in the normal way.
                    prev.next = current.next
                    current = prev  # go back
                else:
                    # We are at the head, advance the head and keep prev as None.
                    head = head.next
            else:
                # Advance the prev pointer.
                prev = current
            # Advance the current pointer.
            current = current.next
        return head
