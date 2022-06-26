class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        res=[]
        for i in range(len(nums)):
            heapq.heappush(res,nums[i])
            if i>=k:
                heapq.heappop(res)
        return heapq.heappop(res)
        