# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            gcd_val = self.gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd_val)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = temp
        return head
            