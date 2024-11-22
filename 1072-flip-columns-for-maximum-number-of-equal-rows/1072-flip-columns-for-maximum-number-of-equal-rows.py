class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        
        for row in matrix:
            
            pattern = "".join("T" if num == row[0] else "F" for num in row)
            
            d[pattern] += 1
            
        return max(d.values())