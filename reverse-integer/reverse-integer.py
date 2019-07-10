class Solution:
    def reverse(self, x: int) -> int:
        try:
            sign = 2 * (x >= 0) - 1
            str_x = str(abs(x))
            rev_x = int(str_x[::-1]) * sign
            if rev_x.bit_length() > 31:
                return 0
            else:
                return rev_x
        except:
            return 0
        
print(Solution().reverse(-321))