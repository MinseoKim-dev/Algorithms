class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        result = []
        
        def dfs(last_index, path):
            if sum(path) == target:
                result.append(path[:])
                return
            elif sum(path) > target:
                return
            else:
                for i in range(last_index, len(candidates)):
                    new_path = path[:]
                    new_path.append(candidates[i])
                    dfs(i, new_path)
        
        dfs(0, [])
        return result
                