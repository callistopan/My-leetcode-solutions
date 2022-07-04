# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow = head
        
        fast = head
        
        
        while fast and fast.next:
            
            slow=slow.next
            
            fast=fast.next.next
            
            if slow == fast:
                
                # there is a cycle
                
                # position slow at the head
                # and increase both the slow and fast one node at a time
                
                slow=head
                
                while slow != fast:
                    
                    slow=slow.next
                    
                    fast=fast.next
                    
                return slow
            
        return None