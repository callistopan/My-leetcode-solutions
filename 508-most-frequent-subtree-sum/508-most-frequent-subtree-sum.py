# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        d={}
        
        # add the sum to the dictionary and increase the count
        
        res=[]
        
        self.dfs(root,d)
        max_freq=float('-inf')
        
        for v in d.values():
            max_freq=max(max_freq,v)
            
        for k,v in d.items():
            if v==max_freq:
                res.append(k)
                
        return res
        
        
        
        
    def dfs(self,root,d):
        
        if not root:
            return 0
        
        sum_ = root.val+self.dfs(root.left,d)+self.dfs(root.right,d)
        
        if sum_ not in d:
            
            d[sum_]=1
            
        else:
            d[sum_]+=1
            
        return sum_
        
        