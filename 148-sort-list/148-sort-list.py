# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        '''only one node or no node'''
        if not head or not head.next :
            return head
        
        ''' find the middle'''
        mid = self.getMid(head)
        
        '''recurse'''
        
        left = self.sortList(head)
        
        right = self.sortList(mid)
        
        return self.merge(left,right)
    
    def merge(self,l1,l2):
        
        dummy= current= ListNode(-1)
        
        while l1 and l2 :
            
            if l1.val <l2.val:
                
                current.next= l1
                
                l1= l1.next
                
                current= current.next
                
            else:
                current.next = l2
                
                l2 = l2.next
                
                current= current.next
                
                
        current.next = l1 if l1 else l2
        
        return dummy.next
    
    
    def getMid(self,head):
        
        prev=None
        
        while head and head.next:
            
            prev = head if not prev else prev.next
            
            head = head.next.next
            
        mid = prev.next
        prev.next =None   # seperate
        
        return mid
            
            
        
                
