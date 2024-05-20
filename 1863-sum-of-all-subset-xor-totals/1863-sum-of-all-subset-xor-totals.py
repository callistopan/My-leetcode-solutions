class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subsetsUtil(A, subset, index,res):
            
            x=0
            for i in range(len(subset)):
                x=x^subset[i]

            res[0]+=x
                
            for i in range(index, len(A)):
                subset.append(A[i])
                subsetsUtil(A, subset, i + 1,res)
                subset.pop(-1)
            return
        
        
        res=[0]
        subset = []
     
        
        index = 0
        subsetsUtil(nums, subset, index,res)
        return res[0]