# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) average time complexity for lookups
        nums_set = set(nums)

        # Create a dummy node to handle edge cases like removing the head node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val in nums_set:
                # Skip the node with a value in nums_set
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return dummy.next
        
        