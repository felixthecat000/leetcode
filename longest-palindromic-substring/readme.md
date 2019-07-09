# Longest palindromic substring

https://leetcode.com/problems/longest-palindromic-substring/
Runtime: 244 ms, faster than 89.67% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.6 MB, less than 23.57% of Python3 online submissions for Longest Palindromic Substring.

### Solution

This one was actually a lot harder than I initially thought. It took a few versions to get to a solution that works in an accepted time.

In the end, the basic strategy used to find palindromes is to start somewhere in the string, either on a single letter or between two adjacent letters and increase the size of the palindrome as long as the next letters on either side are equal. If a palindrome is found, store it and move to the next candidate start location.

To minimise the search, the candidate palindrome starting positions are sorted based on maximum possible length so that if the longest palindrome found is already longer than the remaining candidates in the list we can stop searching.
