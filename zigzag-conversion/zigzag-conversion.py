class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = ['' for i in range(numRows)]
        s = list(s)

        # iterate back and forwards until s has been allocated to rows
        idx = 0
        increment = -1 
        while len(s) > 0:
            rows[idx] += s.pop(0)

            # change direction of iteration if at the ends
            if idx in [0, numRows - 1]:
                increment *= -1

            idx += increment

        return ''.join(rows)
