class Solution:
    ''' time = O(row*col)
        space = O(col)'''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ''' for each row find the maximum area rectangle possible'''
        row=len(matrix)
        col=len(matrix[0])
        dp=[0]*col
        max_area=0
        for r in range(row):
            
            for c in range(col):
                
                dp[c]= 0 if matrix[r][c]=='0' else dp[c]+1
                
            print(dp)
                
            max_area =max(max_area,self.largestRectangleArea(dp))
            
        return max_area
        
          
        
    def largestRectangleArea(self, height):
        
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