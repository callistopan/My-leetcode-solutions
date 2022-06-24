# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1.we use iterative inorder traversal for this problem
    2.use a stack
    3.we append root to stack and try to go to left as much as possible
    4.if root become null then we have to pop from top of stack
    5.decrease k
    6.if k becomes zero then we return ans
    7.else we go further to right
    8.if no right subtree we again pop from stack
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if  k==0:
                return root.val
            root=root.right