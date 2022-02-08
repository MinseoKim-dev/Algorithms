class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_to_list = list(s)
        list_to_set = set(str_to_list)
        maxlength = len(list_to_set)
        while maxlength:
            for i in range(len(s) - maxlength + 1):
                substr = s[i:i + maxlength]
                if len(list(substr)) == len(set(list(substr))):
                    return maxlength
            maxlength -= 1
        return maxlength
