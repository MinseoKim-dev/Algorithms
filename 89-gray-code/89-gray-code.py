class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        else:
            base = self.grayCode(n-1)
            new = [x + 2 ** (n-1) for x in reversed(base)]
            return base + new
            