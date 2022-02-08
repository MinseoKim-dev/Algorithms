class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_formatted_x = str(x)
        comparison = string_formatted_x[::-1]
        
        if string_formatted_x == comparison:
            return True
        else:
            return False