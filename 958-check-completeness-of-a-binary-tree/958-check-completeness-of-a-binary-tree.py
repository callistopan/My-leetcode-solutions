# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
When level-order traversal in a complete tree, after the last node, all nodes in the queue should be null.
Otherwise, the tree is not complete.
'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        end =False
        
        q=deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                
                q.append(node.left)
                q.append(node.right)
                
        return True
                
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
        
        
        