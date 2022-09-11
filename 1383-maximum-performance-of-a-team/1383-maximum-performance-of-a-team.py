class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        #(efficeiency ,speed) => [(9,1),(7,5),(5,2),(4,10),(3,3),(2,8)]
        
        engineers = list(zip(efficiency,speed))
        engineers.sort(reverse=True)
        minHeap=[]
        speedSum=0
        ans=0
        
        for e ,s in engineers:
            speedSum+=s
            heappush(minHeap,s)
            
            if len(minHeap)>k:
                speedSum-=heappop(minHeap) #remove the lowest speed
                
            ans= max(ans,speedSum*e)
        return ans%(10**9+7)