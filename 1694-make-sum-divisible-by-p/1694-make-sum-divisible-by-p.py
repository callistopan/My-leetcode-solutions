class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p == 0:
            return 0

        target = sum(nums)%p;
        dic,n = {0:-1},len(nums)
        cur , ret = 0,n

        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if (cur-target)%p in dic:
                ret = min(ret, i -dic[(cur-target)%p]) 

            dic[cur] = i

        return ret if ret < n else -1
