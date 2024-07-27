class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        res = 0
        d =[[inf]*26 for i in range(26)]
        
        for i in range(len(original)):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')
            d[s][t] = min(d[s][t], cost[i]) # choose the minimum cost
        
        # find the least cost
        for k in range(26): # intermediate between i and j
            for i in range(26):
                for j in range(26):
                    if d[i][k] < inf and d[k][j] < inf:
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        # go through the source and change it to target
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            if d[s][t] >= inf:
                return -1
            res += d[s][t]
            
        return res
        