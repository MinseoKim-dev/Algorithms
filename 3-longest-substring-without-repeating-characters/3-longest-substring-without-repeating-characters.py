class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total_max = 0
        start = 0
        used = {}
        
        if len(s) < 2:
            return len(s)
        
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                total_max = max(total_max, i - start + 1)
            
            used[char] = i
            
        return total_max
            
                