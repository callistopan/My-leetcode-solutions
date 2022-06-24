"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        p=root
        
        if p==None:
            return
        p.next=None
        
        
        while p:
            q=p
            while q:
                if q.left:
                    if q.right:
                        q.left.next=q.right
                    else:
                        q.left.next=self.find_next(q)
                if q.right:
                    q.right.next=self.find_next(q)
                q=q.next
            if p.left:
                p=p.left
            elif p.right:
                p=p.right
            else:
                p=self.find_next(p)
        return root
    def find_next(self,p):
        temp=p.next
        while temp:
            if temp.left:
                return temp.left
            if temp.right:
                return temp.right
            temp=temp.next
        return None
                
                
                
                