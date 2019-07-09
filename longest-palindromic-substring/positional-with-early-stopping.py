class Solution:
    def longestPalindrome(self, s: str) -> str:

        s_len = len(s)

        # handle small cases
        if s_len < 2:
            return ''
        if s_len == 2:
            if s[0] == s[1]:
                return s
            else:
                return ''

        def get_max_len(pos_left, pos_right):
            """
            Auxiliary function for early stopping criteria.
            Calculates the maximum palindrome length from starting position.
            """

            left = pos_left + 1 # maximum size on the left
            right = s_len - pos_right # maximum size on the right
            max_size = min(left, right) * 2
            adjustment = int(pos_left == pos_right) # if odd length palindrome
            return max_size - adjustment

        def longest_palindrome_from_start_position(pos_left, pos_right):

            if pos_left == pos_right:
                pos_left = pos - 1
                pos_right = pos + 1

            candidate = ''

            while pos_left >= 0 and pos_right < s_len and (s[pos_left] == s[pos_right]):

                candidate = s[pos_left:(pos_right + 1)]
                pos_left -= 1
                pos_right += 1

            return candidate


        # list of start positions, starting in the middle
        start_positions = []
        for x in range(1, s_len): 
            start_positions.append([[x-1, x], get_max_len(x-1, x)])
            start_positions.append([[x, x], get_max_len(x, x)])
          
        start_positions = sorted(start_positions, key = lambda x: x[1], reverse=True)
        print(start_positions)

        # starting value
        longest_palindrome = ''

        """
        for start_pos, max_len in start_positions:
            # exit loop process if candidate length is less than already found longest palindromw
            if len(longest_palindrome) > max_len:
                break

            # get candidate and update if it is the new longest palindrome
            print(start_pos)
            candidate = longest_palindrome_from_single_position(start_pos)
            if len(candidate) > len(longest_palindrome):
                longest_palindrome = candidate

        return longest_palindrome
        """

print(Solution().longestPalindrome("aaaa"))
# "babad" "cbbd"