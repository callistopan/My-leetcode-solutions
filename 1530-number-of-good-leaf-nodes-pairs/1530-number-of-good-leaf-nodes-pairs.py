# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Check pairs
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        nonlocal count
                        count += 1

            # Return distances incremented by 1
            return [d + 1 for d in left_distances + right_distances if d + 1 <= distance]
    
        count = 0
        dfs(root)
        return count
    
    
    #T(n)=2*T(n/2)+O(n**2)
    #solve using masters theorem
    #a=2,b=2,k=2   and a<b**k (2<2**2) hence n**k  ==>n**2
    
    #master's theorem-https://www.google.com/url?sa=i&url=https%3A%2F%2Franderson112358.medium.com%2Fmaster-theorem-909f52d4364&psig=AOvVaw1dActLWLJ1sXKa26x296Mc&ust=1646990848121000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJDvgvGdu_YCFQAAAAAdAAAAABAD