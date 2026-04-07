class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) <= 1:
            return 0
        low = 0

        for high in range(1, len(prices)):
            if prices[high] < prices[low]:
                low = high
            
            else:
                maxProfit = max(maxProfit, prices[high] - prices[low])
        return maxProfit
