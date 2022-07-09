# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],partial_sum=0) -> int:
        
        if not root:
            return 0
        
        partial_sum = partial_sum*2 + root.val
        
        if not root.left and not root.right:
            return partial_sum
        
        return self.sumRootToLeaf(root.left,partial_sum) + self.sumRootToLeaf(root.right,partial_sum)
        
        
        