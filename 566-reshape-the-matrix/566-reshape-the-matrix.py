class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows = len(mat)
        columns = len(mat[0])
        if rows*columns != r*c:
            return mat
        
        result = []
        
        
        for i in range(r):
            row = []
            for j in range(c):
                index = i*c + j
                row.append(mat[index//columns][index%columns])
            
            result.append(row)
            
        return result