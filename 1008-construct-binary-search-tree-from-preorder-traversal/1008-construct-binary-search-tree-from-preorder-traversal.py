# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        def build(l,r):
            
            if root_index[0]==len(preorder):
                return None
            
            root_data=preorder[root_index[0]]
            
            if  not l< root_data <r:    # we cannot insert
                return None
            
            root_index[0]+=1
            
            left=build(l,root_data)
            right=build(root_data,r)
            
            return TreeNode(root_data,left,right)   
        
        root_index=[0]
        
        return build(float('-inf'),float('inf'))
        
        
        
        
        
        
        
        
        