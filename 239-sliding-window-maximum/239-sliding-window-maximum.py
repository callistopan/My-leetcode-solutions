class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ''' sliding window of size k  
            there is one maximum element
            for each window we need to add the current maximum
            
            time complexity -O(n)
            It seems more than O(n) at first look. It can be observed that every element of array is added and removed at most once. So there are total 2n operations
            
            space - O(k) deque
            '''
        
        n=len(nums)
        res=[]
        q = deque()
        
        for i in range(k):
            
            while q  and nums[q[-1]]<= nums[i]:
                q.pop()
                
            q.append(i)
        
        print(q)
            
        for i in range(k,n):
            
            res.append(nums[q[0]])
            
            while q and q[0] <= i-k:   # remove out of bound elements
                
                q.popleft()
                
            while q and nums[q[-1]] <= nums[i]:   # remove useless elements
                q.pop()
                
            q.append(i)
            
        
        res.append(nums[q[0]])
        
        return res
        
    
        
        