import heapq
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_val = 0
        ans = []
        pq = []

        for i in range(len(nums)):
            sum_val += nums[i]
            heapq.heappush(pq, (nums[i], i))

        for q in queries:
            sum_val -= nums[q[0]]
            nums[q[0]] = 0

            while pq and q[1]:
                val, idx = heapq.heappop(pq)
                if nums[idx]:
                    sum_val -= nums[idx]
                    nums[idx] = 0
                    q[1] -= 1

            ans.append(sum_val)

        return ans
        
            
            
            