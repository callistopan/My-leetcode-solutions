# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        max_level = [0]
        res=[]
        self.rightViewUtil(root, 1, max_level,res)
        return res
        
    def rightViewUtil(self,root, level, max_level,res):
        if root is None:
            return

            # If this is the last node of its level
        if (max_level[0] < level):
            res.append(root.val)
            max_level[0] = level

            # Recur for right subtree first, then left subtree
        self.rightViewUtil(root.right, level+1, max_level,res)
        self.rightViewUtil(root.left, level+1, max_level,res)