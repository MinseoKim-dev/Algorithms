class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        result = ""
        
        if len(a) >= len(b):
            longer = a
            max_length = len(a)
            min_length = len(b)
        else:
            longer = b
            max_length = len(b)
            min_length = len(a)
        
        add = 0
        
        for i in range(max_length):
            if i < min_length:
                r = int(a[i]) + int(b[i]) + add
                add = 0
                if r > 1:
                    add = 1
                    r -= 2
                result += str(r)
            else:
                r = int(longer[i]) + add
                add = 0
                if r > 1:
                    add = 1
                    r -= 2
                result += str(r)
                
        if add > 0:
            result += str(add)
            
        return result[::-1]