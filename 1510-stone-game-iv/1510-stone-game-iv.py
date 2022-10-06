class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
         after going to the next state, Bob becomes the player removing the stones, which is the position of Alice in the current state. Therefore, to find out whether Bob will lose in the next state, we just need to check whether our function gives False for remaining stones.
        '''
        @lru_cache(None)
        def dfs(remain):
            if remain==0:
                return False
            
            sqrt= int(remain**0.5)
            for i in range(1,sqrt+1):
                # if there is a chance of opponent lose the game 
                
                if not dfs(remain-i*i):
                    return True
                
            return False
        return dfs(n)
        