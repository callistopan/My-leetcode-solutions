# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''using double ended queue
           append to the queue as normal'''
        if not root: return []
        q = deque([root])
        result = []
        level = 0
        
        while q:
            currentnode = deque()
            levelsize = len(q)
            for _ in range(levelsize):
                node = q.popleft()
                if level % 2 == 0:
                    currentnode.append(node.val)
                else:
                    currentnode.appendleft(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(currentnode)
            level += 1
        return result 
                