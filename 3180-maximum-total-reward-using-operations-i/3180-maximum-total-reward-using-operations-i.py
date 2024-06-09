class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        n = len(rewardValues)
        rewardValues.sort()
        
        maxim = rewardValues[-1]
        
        d = [[-1 for _ in range(maxim + 1)] for _ in range(n + 1)]
        
        
        def dfs(i, curr_reward):
           
            if i >= n:
                return 0
            if curr_reward >= maxim:
                return 0
            if d[i][curr_reward] != -1:
                return d[i][curr_reward]
            
        
            take_reward = 0
            skip_reward = 0
            
            if curr_reward < rewardValues[i]:
                take_reward = rewardValues[i] + dfs(i + 1, curr_reward + rewardValues[i])
            skip_reward = dfs(i +1, curr_reward)
            res = max(take_reward, skip_reward)
            d[i][curr_reward] = res
            return res


        return dfs(0, 0)
