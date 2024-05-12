class Solution:
    '''
        Intuition

        Move from c1 to ck with path c1,c2,..,ck,
        res = (c2 - c1) + (c3 - c2) + .... = ck - c1

        Explanation

        To calculate the best score ending at a cell ck,
        just need to find out the minimum c1 on its top left area.
    '''
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = -inf
        for i in range(m):
            for j in range(n):
                pre = min(grid[i-1][j] if i else inf, grid[i][j-1] if j else inf) # top left
                res = max(res, grid[i][j] - pre)
                grid[i][j] = min(grid[i][j],pre)
        return res
        
        