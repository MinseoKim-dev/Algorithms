class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(element, path):
            if not len(element):
                result.append(path[:])
            
            for e in element:
                remainder = element[:]
                remainder.remove(e)
                curr_path = path[:]
                curr_path.append(e)
                dfs(remainder, curr_path)
        
        dfs(nums, [])
        return result