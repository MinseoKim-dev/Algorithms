class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        digit = 1
        count = 0
        for i in range(length-1, -1, -1):
            count += (ord(columnTitle[i])-64) * digit
            digit *= 26
        return count
            
    
            
            