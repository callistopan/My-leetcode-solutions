class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        ans = [(rStart,cStart)]
        if rows * cols ==1:
            return ans

        # for walk length k = 1,3,5,7...

        for k in range(1,2*(rows+cols),2):

            for dr,dc,dk in ((0,1,k),(1,0,k),(0,-1,k+1),(-1,0,k+1)):

                for _ in range(dk): # walk in this direction for dk times

                    rStart += dr
                    cStart += dc

                    if 0 <=rStart < rows and 0 <= cStart <cols:
                        ans.append((rStart,cStart))
                        if len(ans) == rows * cols:
                            return ans
        