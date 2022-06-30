class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' the idea is splitting the array into to parts left and right
            compute maximum for left and max for right in reverse order
            and sum these two'''
        max_total_profit=0
        min_price_so_far=float("inf")
        
        first_buy=[0]*len(prices)
        
        # forward
        
        for i ,price in enumerate(prices):
            min_price_so_far=min(min_price_so_far,price)
            max_total_profit=max(max_total_profit,price-min_price_so_far)
            first_buy[i]=max_total_profit
            
            
        # backward phase maximum profit if we make a second by on that day
        
        max_price_so_far=float('-inf')
        
        for i ,price in reversed(list(enumerate(prices[1:],1))):
            max_price_so_far=max(max_price_so_far,price)
            
            max_total_profit=max(max_total_profit,max_price_so_far-price+first_buy[i-1])
        return max_total_profit
        
        