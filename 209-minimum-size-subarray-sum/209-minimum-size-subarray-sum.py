class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curr_sum=0
        min_len=float("inf")
        n=len(nums)
        
        for i in range(n):
            curr_sum+=nums[i]
            
            while curr_sum>=target:
                min_len=min(min_len,i-left+1)
                curr_sum-=nums[left]
                left+=1
        return min_len if min_len!=float("inf") else 0