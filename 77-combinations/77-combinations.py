class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        
        def dfs(start, path):
            if len(path) == k:
                result.append(path[:])
            
            for i in range(start, n+1):
                cur_path = path[:]
                cur_path.append(i)
                dfs(i+1, cur_path)
            
        
        dfs(1, [])
        return result
            