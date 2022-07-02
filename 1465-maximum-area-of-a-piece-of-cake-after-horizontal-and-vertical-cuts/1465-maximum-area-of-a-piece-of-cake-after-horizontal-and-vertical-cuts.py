class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts=[0]+  horizontalCuts+[h]
        
        verticalCuts=[0] + verticalCuts+[w]
        
        horizontalCuts.sort()
        
        verticalCuts.sort()
        
        max_h=float("-inf")
        
        max_v=float("-inf")
        
        for i in range(1,len(horizontalCuts)):
            
            max_h= max(max_h,horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1,len(verticalCuts)):
            
            max_v= max(max_v,verticalCuts[i]-verticalCuts[i-1])
            
            
        return (max_h *max_v)%(10**9+7)
        
        
        
        
        
        