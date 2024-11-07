class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans=0
        
        '''if at same position count the number of 1 bits as these will only result int a positive number'''
        for i in range(32):
            curr=0
            for num in candidates:
                curr+=(num >>i)&1
            ans=max(ans,curr)
        return ans