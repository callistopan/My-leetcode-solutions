# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache(None)
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        is_even = True
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if is_even:
                    if node.val % 2 == 0: return False
                    if prev and prev.val >= node.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and prev.val <= node.val: return False
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                prev = node
            is_even = not is_even
        return True