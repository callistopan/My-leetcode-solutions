# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q= deque()
        
        q.append(root)
        
        res=[]
        level=0
        
        while q :
            
            l=len(q)
            s=0
            
            for i in range(l):
                
                node=q.popleft()
                
                s+=node.val
                
                if node.left:
                    
                    q.append(node.left)
                    
                if node.right:
                    
                    q.append(node.right)
                    
            res.append(s/l)
        return res