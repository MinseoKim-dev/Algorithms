class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def bfs(start, current):
            result.append(current)
            
            for i in range(start, len(nums)):
                new = current[:]
                new.append(nums[i])
                bfs(i+1, new)
        
        bfs(0, [])
        return result