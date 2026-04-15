class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  
        min_price = prices[0]
        max_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                max_price = prices[i]
            else:
                profit += max_price - min_price
                max_price = prices[i]
                min_price = prices[i]
        profit += max_price - min_price           
        return profit