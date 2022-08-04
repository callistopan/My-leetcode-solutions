class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min=prices[0]
        profit=0
        
        for price in prices:
            profit=max(profit,price-current_min)
            current_min=min(current_min,price)
        return profit