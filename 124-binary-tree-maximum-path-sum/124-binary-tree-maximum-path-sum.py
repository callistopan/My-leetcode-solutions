# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max_path=float("-inf")
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            
        self.maxPathSumhelp(root)
            
        return self.max_path
        
    def maxPathSumhelp(self, root: Optional[TreeNode]) -> int:
            
        if root==None:
            return 0
        
        # for avoiding the negative we need to limit to zero
            
        l=max(self.maxPathSumhelp(root.left),0)
            
        r=max(self.maxPathSumhelp(root.right),0)
            
        current_max=root.val+l+r
            
        self.max_path=max(self.max_path,current_max)

        return root.val+max(l,r)
    
        
    