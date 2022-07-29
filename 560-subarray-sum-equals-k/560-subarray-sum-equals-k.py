class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        
        count=0
        
        sum_=0
        
        for i in range(len(nums)):
            
            sum_+=nums[i]
            
            if sum_==k:
                count+=1
                
            if sum_-k in d:
                count+=d[sum_-k]
                
            if sum_ not in d:
                
                d[sum_]=1
                
            else:
                d[sum_]+=1
                
        return count
            