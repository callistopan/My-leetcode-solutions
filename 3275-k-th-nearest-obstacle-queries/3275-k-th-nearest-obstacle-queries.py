from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        l = SortedList()
        
        res = []
        
        for x, y in queries:
            l.add(abs(x) + abs(y))
            if len(l) >= k:
                res.append(l[k-1])
            else:
                res.append(-1)
        return res