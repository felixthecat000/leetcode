class Solution:
    def myAtoi(self, s: str) -> int:

        # define extreme return vals
        max_32 = 2**31 - 1
        min_32 = 0 - 2**31

        try:
            # find valid digits
            s = s.lstrip(' ')
            digit_len = len(s) - len(s.lstrip('-+0123456789'))
            digit_str = s[:digit_len]

            # a dash/plus sign not first place invalidates subsequent numbers
            digit_str = digit_str[0] + digit_str[1:].split('-')[0].split('+')[0]

            val = int(digit_str)
            if val >= 0:
                return min(max_32, val)
            else:
                return max(min_32, val)
        except:
            return 0
