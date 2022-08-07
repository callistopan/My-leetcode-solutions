import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        
        total = sum(nums)
        
        half = total/2
        
        count=0
        
        while True:
            
            curr_max=-heapq.heappop(heap)
            total-= curr_max/2
            
            count+=1
            
            if total<= half:
                return count
            
            heapq.heappush(heap,-curr_max/2)
            