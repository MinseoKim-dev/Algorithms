class Solution:
    def mySqrt(self, x: int) -> int:
        def recursive_binary_search(x, start, end):
            mid = (start+end)//2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif mid**2 > x:
                return recursive_binary_search(x, start, mid-1)
            else:
                return recursive_binary_search(x, mid+1, end)
        
        return recursive_binary_search(x, 0, x)
            