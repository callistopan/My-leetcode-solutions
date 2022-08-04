# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        memo={0:[],1:[TreeNode(0)]}
        
        return self.generate(n,memo)
        
    def generate(self,n,memo):
        
        if n in memo:
            return memo[n]
        if n==0:
            return [None]

        result=[]

        for left_nodes in range(n):
            right_nodes=n-1-left_nodes

            left=self.generate(left_nodes,memo)
            right=self.generate(right_nodes,memo)

            # generate all combinations of left and right subtrees
            result+=[TreeNode(0,l,r) for l in left for r in right if (l and r) or (not l and not r)]
            
        memo[n]=result

        return result

        