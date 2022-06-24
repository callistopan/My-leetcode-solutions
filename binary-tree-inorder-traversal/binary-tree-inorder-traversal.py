# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #return self.inorder_recursive(root)
        return self.inorder_iter(root)
        
        
    def inorder_recursive(self,root):
        if not root:
            return []
        
        return self.inorder_recursive(root.left)+[root.val]+self.inorder_recursive(root.right)
    
    
    def inorder_iter(self,root):
        res=[]
        stack=[]
        curr=root
        while curr or stack:
            
            while curr:
                stack.append(curr)
                curr=curr.left
                
            temp=stack.pop()
            res.append(temp.val)
            curr=temp.right
        return res
            
            
                
                
    
        