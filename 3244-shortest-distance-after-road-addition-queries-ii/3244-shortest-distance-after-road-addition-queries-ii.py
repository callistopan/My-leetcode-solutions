from sortedcontainers import SortedList
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        curr = SortedList()
        
        for i in range(n):
            curr.add(i)
        #print(curr)
        
        ans = []
        
        rest = n - 1
        
        for l, r in queries:
            locl = curr.bisect(l)
            locr = curr.bisect_left(r)
            
            #print(locl,locr, curr)
            for i in range(locr - locl):
                curr.pop(locl)
                rest -= 1
                
            ans.append(rest)
        return ans