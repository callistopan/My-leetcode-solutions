class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[left], height[right]) * (right - left), result)
            if height[left] <height[right]:
                left+=1
            
            else:
                right-=1
                
        return result
'''when ai < aj, if we move j to the left:
1. the length on x-axis will definitly decrease
2. if a(j-1) > ai, the area will be ai * length on x-axis which is smaller than original area
3. if a(j-1) < ai, the area will be a(j-1) * length on x-axis which is also smaller than original area
so moving j to the left won't give us a larger area, we can only move i to the right to get a possible larger area.'''