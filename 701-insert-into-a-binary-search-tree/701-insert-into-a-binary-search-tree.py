# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)
        
#         if root.val>val:
#             root.left=self.insertIntoBST(root.left,val)
#         else:
#             root.right=self.insertIntoBST(root.right,val)
#         return root
          return self.insert_iter(root,val)
    
    def insert_iter(self,root,val):
        node=TreeNode(val)
        temp=root
        
        while temp:
            if temp.val>val:
                if temp.left:
                    temp=temp.left
                else:
                    temp.left=node
                    break
            else:
                if temp.right:
                    temp=temp.right
                else:
                    temp.right=node
                    break
        return root if root else node
                    
                    