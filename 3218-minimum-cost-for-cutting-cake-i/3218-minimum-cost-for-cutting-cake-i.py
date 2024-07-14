class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        M = m
        N = n
        
        @cache
        def dfs(si, ei, sj, ej):
            if ei - si == 1 and ej - sj == 1:
                return 0
            cost = inf
            
            for i in range(si+1,ei):
                cost = min(cost, horizontalCut[i-1]+ dfs(si,i,sj,ej) + dfs(i,ei,sj,ej))
            for j in range(sj+1, ej):
                cost = min(cost, verticalCut[j-1] + dfs(si,ei,sj,j) + dfs(si,ei,j,ej))
            return cost
        return dfs(0,m,0,n)