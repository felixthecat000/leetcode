# Longest palindromic substring

https://leetcode.com/problems/longest-palindromic-substring/

Basic strategy to find palindromes is to start somewhere in the string, either on a single letter or between two adjacent letters and increase the size of the palindrome as long as the next letters on either side are equal.

To minimise the search, the candidate palindrome starting positions are sorted based on maximum possible length so that if the longest palindrome found is already longer than the remaining candidates in the list we can stop searching.
