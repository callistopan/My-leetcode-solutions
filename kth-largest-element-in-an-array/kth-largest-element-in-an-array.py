class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        for i in range(len(nums)-k+1):
            k=heapq.heappop(nums)
        return k
        