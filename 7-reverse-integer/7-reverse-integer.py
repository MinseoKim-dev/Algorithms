class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        flag = 1
        if str_num[0] == "-":
            flag = 0
            str_num = str_num[1:]
        reversed = str_num[::-1]
        rev_num = int(reversed)
        if flag:
            answer = rev_num
        else:
            answer = -rev_num
        if answer < -(2 ** 31) or answer >= 2 ** 31:
            return 0
        else:
            return answer
