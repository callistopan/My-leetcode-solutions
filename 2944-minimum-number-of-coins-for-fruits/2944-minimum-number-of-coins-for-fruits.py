from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        memo = {}
        return self.dfs(prices, 0, memo)

    def dfs(self, prices: List[int], index: int, memo: dict) -> int:
        if index in memo:
            return memo[index]
        if index >= len(prices):
            return 0

        min_cost = float('inf')

        # Buy the current fruit and jump to index + index + 2
        min_cost = min(min_cost, prices[index] + self.dfs(prices, index + index + 2, memo))

        # Buy any of the next fruits in the range [index + 1, index + index + 1]
        for i in range(index + 1, index + index + 2):
            if i < len(prices):
                min_cost = min(min_cost, prices[index] + self.dfs(prices, i, memo))

        memo[index] = min_cost
        return min_cost

