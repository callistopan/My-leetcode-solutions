class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = i = 0
        count = 0
        for j in range(len(nums)):
            
            if nums[j]%2==1:
                k-=1
                count=0
                
            
            # we have required k odd numbers so we try to reduce the window    
            while k==0:
                
                k+=nums[i]&1
                
                i+=1
                count+=1
            print(res)
            res+=count
            
        return res
                
            
                
            