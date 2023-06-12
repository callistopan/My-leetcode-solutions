class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret=[]
        save=""
        for i in range(len(nums)):
            if i<=len(nums)-2 and nums[i+1]==nums[i]+1:   #these are the conditions for range ending 
                if save=="": save=str(nums[i])+"->"
            else:
                ret.append(save+str(nums[i]))
                save=""

        return ret        
            
                