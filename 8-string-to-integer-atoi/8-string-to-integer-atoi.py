class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        sign = {'+', '-'}
        s = s.strip()
        if len(s) == 0:
            return 0
        flag = 1
        if s[0] == '+':
            flag = 1
            s = s[1:]
        elif s[0] == '-':
            flag = 0
            s = s[1:]

        result = []

        for letter in s:
            if letter in digits:
                result.append(letter)
            else:
                break

        new_str = "".join(result)
        if len(result) == 0:
            return 0
        ans = int(new_str)

        if not flag:
            ans = -ans

        if ans >= 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        elif ans < -2 ** 31:
            ans = -2 ** 31

        return ans