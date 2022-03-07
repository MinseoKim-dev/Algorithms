class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        def recursive_fill(image, r, c, cur_color, new_color, visited):
            
            if (r, c) in visited:
                return
            rows = len(image)
            columns = len(image[0])
            visited.append((r, c))
            
            if image[r][c] == cur_color:
                image[r][c] = new_color
                if r-1 >= 0:
                    recursive_fill(image, r-1, c, cur_color, new_color, visited)
                if c-1 >= 0:
                    recursive_fill(image, r, c-1, cur_color, new_color, visited)
                if r+1 < rows:
                    recursive_fill(image, r+1, c, cur_color, new_color, visited)
                if c+1 < columns:
                    recursive_fill(image, r, c+1, cur_color, new_color, visited)
        
        recursive_fill(image, sr, sc, image[sr][sc], newColor, [])
        return image
                    
                