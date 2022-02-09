class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_pr = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            min_pr = min(min_pr, prices[i])
            profit = max(profit, prices[i]-min_pr)
            
        return profit