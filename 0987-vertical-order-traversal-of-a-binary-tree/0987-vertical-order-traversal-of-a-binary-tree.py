# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = defaultdict(list) 
        queue = deque([(root, 0)])
        x_min, x_max = 0, 0
        while queue:
            tmp = defaultdict(list)
            for _ in range(len(queue)):
                node, x = queue.popleft()
                tmp[x].append(node.val) 
                if node.left:
                    queue.append((node.left, x-1))
                    x_min = min(x_min, x-1)
                if node.right: 
                    queue.append((node.right, x+1)) 
                    x_max = max(x_max, x+1)
            for i in tmp: 
                mapping[i] += sorted(tmp[i])
        return [mapping[i] for i in range(x_min, x_max+1)]