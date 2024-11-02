import math
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        

        
        @cache
        def dfs(i, first, second):
            
            if i == len(nums):
                return (first and  second) and (first == second)

            
            skip = dfs(i+1, first, second)
            
            takeFirst = dfs(i+1, math.gcd(first,nums[i]), second)
            
            takeSecond = dfs(i + 1, first, math.gcd(second, nums[i]))
            
            # sum up all the possibilites
            
            return (skip + takeFirst + takeSecond) % (10**9 + 7)  
        
        return dfs(0,0,0)