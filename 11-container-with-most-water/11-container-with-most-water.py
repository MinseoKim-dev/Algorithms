class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #area = (i2 - i1) * min(height[i1], height[i2])
        
        start = 0
        end = len(height)-1
        ans = 0
        
        while start <= end:
            ans = max(ans, (end - start) * min(height[end], height[start]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        
        return ans