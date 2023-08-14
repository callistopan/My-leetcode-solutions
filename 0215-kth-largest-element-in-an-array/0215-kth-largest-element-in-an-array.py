class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        import heapq
        for num in nums:
            heapq.heappush(heap,-(num))
        res=0
        for i in range(k):
            res=heapq.heappop(heap)
        return -(res)
        