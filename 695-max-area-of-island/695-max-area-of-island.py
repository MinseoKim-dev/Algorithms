class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        
        def recursive_search(r, c):
                
            a1, a2, a3, a4 = 0, 0, 0, 0
            
            if r < 0 or c < 0 or r >= rows or c >= columns:
                return 0
            
            
            if not grid[r][c]:
                return 0
            
            if grid[r][c]:
                grid[r][c] = 0
                if r-1 >= 0:
                    a1 = recursive_search(r-1, c)
                if c-1 >= 0:
                    a2 = recursive_search(r, c-1)
                if r+1 < rows:
                    a3 = recursive_search(r+1, c)
                if c+1 < columns:
                    a4 = recursive_search(r, c+1)
                return 1 + a1 + a2 + a3 + a4
            
        result = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    ans = recursive_search(i, j)
                    result = max(result, ans)
        
        return result