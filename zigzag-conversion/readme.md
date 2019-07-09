# Zig Zag Conversion

https://leetcode.com/problems/zigzag-conversion/submissions/
Runtime: 76 ms, faster than 48.72% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.

### Solution

Pretty simple strategy, although the question asks for a zig-zag pattern, the return string does not contain those spaces. All that happens is that string s is allocated across numRows in a backwards and forwards iteration.

In this solution we do exactly that, creating a string for each row and adding to it as we iterate. At the end, the return value joins the rows together into a single string.
