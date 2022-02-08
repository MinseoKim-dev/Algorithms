class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        target = strs[0]
        
        for i in range(len(target)):
            count = 0
            for j in range(1, len(strs)):
                if len(strs[j]) > i:
                    if target[i] == strs[j][i]:
                        count += 1
                    else:
                        break
            if count == len(strs)-1:
                result += target[i]
            else:
                break
        
        return result