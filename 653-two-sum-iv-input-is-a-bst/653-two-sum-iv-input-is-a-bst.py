# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # time o(n)
        # space o(h)
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right
        
        '''pop from the stack and if node has any right node then push that and its left too
           so that we get the smallest element at the top of the stack'''
        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val
        
        ''' the stLeft stack contain smaller elements at the top
             the stRight stack contian larger elements at the top'''
        stLeft, stRight = [], []
        ''' initially push leftmost and right most'''
        pushLeft(stLeft, root)
        pushRight(stRight, root)
        
        ''' if leftsum+rightsum less than k then we need to consider the next left
            else we need to consider the next right'''
        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False