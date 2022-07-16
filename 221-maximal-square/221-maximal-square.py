class Solution:
    '''time and space is O(m*n)'''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # first row containing all the squares of area 1 similiarly first column
        # if a cell need to form a square all the cells above containing 1
        # if a cell is 0 just ignore it
        
        r =len(matrix)
        
        c =len(matrix[0])
        
        dp=[[0 for j in range(c)] for i in range(r)]
        
        # first row
        max_width=0
        
        for j in range(c):
            if matrix[0][j]=='1':
                max_width=1
                
            
            dp[0][j]=1 if matrix[0][j]=='1' else 0
            
        # first column
        
        for i in range(r):
            
            if matrix[i][0]=='1':
                max_width=1
                
            
            dp[i][0]=1 if matrix[i][0]=='1' else 0
            
        # remaining cells
        

        
        for i in range(1,r):
            
            for j in range(1,c):
                
                if matrix[i][j]=='1':
                    
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    
                max_width=max(max_width,dp[i][j])
                
        return max_width**2
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                