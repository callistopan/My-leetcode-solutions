class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ''' sliding window of size k  
            there is one maximum element
            for each window we need to add the current maximum'''
        
        n=len(nums)
        res=[]
        q = deque()
        
        for i in range(k):
            
            while q  and nums[q[-1]]<= nums[i]:
                q.pop()
                
            q.append(i)
            
        for i in range(k,n):
            
            res.append(nums[q[0]])
            
            while q and q[0] <= i-k:
                
                q.popleft()
                
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            q.append(i)
            
        
        res.append(nums[q[0]])
        
        return res
        
    
        
        