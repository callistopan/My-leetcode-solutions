class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(j, count):
            if count == 4:  # We have chosen 4 elements from b
                return 0
            if j >= len(b):  # If we've exhausted all elements in b
                return float('-inf')

            # Option 1: Choose the current b[j] for a[count] and move to the next index
            choose = a[count] * b[j] + dfs(j + 1, count + 1)

            # Option 2: Skip the current b[j] and try the next one
            skip = dfs(j + 1, count)

            return max(choose, skip)
        return dfs( 0, 0)