class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        c =Counter(nums)
        
        nums.sort()
        count=0
        
        for i in c:
            
            if (k>0 and i+k in c) or (k==0 and c[i]>1):
                
                count+=1
                
        return count