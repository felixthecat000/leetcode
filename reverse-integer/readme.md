# Reverse Integer

https://leetcode.com/problems/reverse-integer/

Runtime: 36 ms, faster than 81.44% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.2 MB, less than 69.06% of Python3 online submissions for Reverse Integer.

### Solution

Convert to string, reverse it and convert back to integer. Some handling of negative values also.

### Things I Learned

The integer method int().bit_length()

Since Python3 integers will increase in size to match the input we need to manually check for the size of the integer created. The easiest way to do this I found was in the built in class method 'bit_length()'.
