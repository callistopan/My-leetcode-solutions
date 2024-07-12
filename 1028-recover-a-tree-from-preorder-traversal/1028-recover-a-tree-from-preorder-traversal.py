# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        while i < n:
            level = 0
            value = ""
            
            while i < n and traversal[i] == '-':
                level +=1
                i +=1
            
            while i < n and traversal[i].isdigit():
                value += traversal[i]
                i +=1
            
            node = TreeNode(int(value))
            
            while len(stack) > level:
                stack.pop()
            
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
            
        return stack[0]