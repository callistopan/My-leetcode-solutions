# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if root==p or root== q :
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        
        if left and right :
            
            return root
        
        if not left and not right:
            return None
        
        return left if left else right
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def recurse_tree(node):
#             if not node:#reached leaf node
#                 return False
#             left=recurse_tree(node.left)
#             right=recurse_tree(node.right)
            
#             found_one=node==p or node==q
            
#             if found_one+left+right>=2:
#                 self.ans=node
#                 return True
#             return found_one or left or right
        
        
        
#         recurse_tree(root)
#         return self.ans
        