class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def dfs(index, path):
            if index >= len(s):
                result.append(path)
                return
            if s[index].isupper():
                dfs(index+1, path + s[index].lower())
                dfs(index+1, path + s[index])
            elif s[index].islower():
                dfs(index+1, path + s[index].upper())
                dfs(index+1, path + s[index])
            else:
                dfs(index+1, path + s[index])
        
        dfs(0, "")
        return result