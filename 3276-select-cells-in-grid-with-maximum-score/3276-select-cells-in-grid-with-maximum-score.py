class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        values = []
        
        # separate all the values and save it's coordinates
        for i in range(n):
            for j in range(m):
                values.append((grid[i][j], i, j))
        
        # sort the values so we will get maximum at first
        values.sort(reverse = True)
        memo = {}
        
        return self.dfs(values, 0, 0, memo)
        
    def dfs(self, values, i, mask_row, memo):
        
        n = len(values)
        if i == n: # gone through all the cells
            return 0
        
        if (i, mask_row) in memo: # if we have seen this state before
            return memo[(i, mask_row)]
        
        ans = 0
        row_number = values[i][1] 
        
        if 1 << row_number & mask_row: # This will check if this row number has been taken before reaching this state
            ans += self.dfs(values, i + 1, mask_row, memo) # skip this value
        else: # the row number has never seen before
            
            j = i 
            while j < n and values[i][0] == values[j][0]: # find a unique value
                j += 1
                
            take = values[i][0] + self.dfs(values, j, (1 << row_number) | mask_row, memo) # take the value and mark the row number as taken
            not_take = self.dfs(values, i + 1, mask_row, memo)
            
            ans = max(take, not_take)
        memo[(i, mask_row)] = ans
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        