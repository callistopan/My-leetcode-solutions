class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for num in nums:
            x = x ^ num
        ans = x ^ k
        count = 0
        while ans:
            ans &= (ans -1)
            count+=1
        return count
