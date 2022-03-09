class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
        
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for key, value in dic.items():
            if value == 1:
                return s.index(key)
        
        return -1