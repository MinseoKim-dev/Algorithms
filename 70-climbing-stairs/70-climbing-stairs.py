class Solution:
    def climbStairs(self, n: int) -> int:
        #Use Dynamic Programming
        
        dp = [1, 2]
        
        if n == 1:
            return dp[0]
        if n == 2:
            return dp[1]
        
        while len(dp) < n:
            dp.append(dp[-1] + dp[-2])
        
        return dp[-1]