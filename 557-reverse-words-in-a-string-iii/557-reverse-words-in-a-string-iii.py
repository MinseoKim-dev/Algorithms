class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        converted = s.split()
        for i in range(len(converted)):
            converted[i] = converted[i][::-1]
        
        return " ".join(converted)