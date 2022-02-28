class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[math.comb(j, i) for i in range(j+1)] for j in range(numRows)]