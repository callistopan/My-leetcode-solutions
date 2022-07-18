class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans
        
#         res =[]
        
#         self.backtrack(nums,0,[],res)
        
#         return res
    
    
#     def backtrack(self,nums,index,current,res):
        
        
#         if index>=len(nums):
#             return
#         res.append(current[:])
        
        
#         for i in range(index,len(nums)):
#             print(nums[i])
            
#             current.append(nums[i])
            
#             self.backtrack(nums,index+1,current,res)
            
#             current.pop()
            
            
            
            
                