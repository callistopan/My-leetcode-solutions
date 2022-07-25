import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        
        startTime = [jobs[i][0] for i in range(n)]
        max_profit=0
        dp = [0] * (n + 1)  # profit up to this point
        for i in range(n-1, -1, -1):
            j = bisect_left(startTime, jobs[i][1])  # find insertion point of end time of current in start time array
            
            dp[i] = max(dp[i], dp[j] + jobs[i][2],max_profit) # profit at end time + current profit
            
            if dp[i]>max_profit:
                    max_profit=dp[i]
            
                    
        return max_profit
    
    
   










    
#     n = len(startTime)
#         jobs = sorted(list(zip(startTime, endTime, profit)))
#         startTime = [jobs[i][0] for i in range(n)]

#         @lru_cache(None)
#         def dp(i):
#             if i == n: return 0
#             ans = dp(i + 1)  # Choice 1: Don't pick

#             j = bisect_left(startTime, jobs[i][1])
#             ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
#             return ans

#         return dp(0)
        
        
        
#         n = len(startTime)
#         jobs = sorted(list(zip(startTime, endTime, profit)))
#         memo={}

#         def dfs(i):
#             if i == n: return 0
#             if i in memo: return memo[i]
#             ans = dfs(i + 1)  # Choice 1: Don't pick

#             for j in range(i + 1, n + 1):
#                 if j == n or jobs[j][0] >= jobs[i][1]:
#                     ans = max(ans, dfs(j) + jobs[i][2])  # Choice 2: Pick
                    
#                     break

#             memo[i] = ans

#             return ans

#         return dfs(0)