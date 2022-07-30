# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''fix the left and right and decide deletion'''
        if not root:
            return None
        
        root.left = self.trimBST(root.left,low,high)
        
        root.right= self.trimBST(root.right,low,high)
        
        # fix root
        
        if root.val <low :
            return root.right   # as everything left is less than root
        
        if root.val >high:
            return root.left  # as everything right is even higher than root
        
        return root
            