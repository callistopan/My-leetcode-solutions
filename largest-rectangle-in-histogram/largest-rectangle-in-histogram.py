class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        
        ''' if the height of current bar is less than the stack top one 
            then height of possible rectangle is hight of top stack
            and width is current index - the current stack top element index -1
            for computing the last possible area we append 0 to the height'''
        
        
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        
        return ans