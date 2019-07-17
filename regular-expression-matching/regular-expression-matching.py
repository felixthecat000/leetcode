class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def parse_char(s_remainder, char, star=False):
            """
            Match only the current character.
            Returns unmatched part of s if successful or None if match incorrect.
            """
            
            # set match char if wild card
            if char == '.':
                char = s[0]

            if s[0] != char:
                if star:
                    return s_remainder
                else:
                    return ''

            # if in 'star' mode get run of same characters
            i = 1
            if star:
                while (len(s) > i and (s[i] == s[0])):
                    i += 1

            return s[i:]

        def select_char(pattern):
            
            # check for star
            if len(pattern) > 1:
                if pattern[1] == '*':
                    return pattern[0], True, pattern[2:]
            
            # otherwise return standard match
            return pattern[0], False, pattern[1:]

        while len(s) > 0 and len(p) > 0:
            char, star, p = select_char(p)
            s = parse_char(s, char, star)

        if len(s) == 0 and len(p) == 0:
            return True
        else:
            return False

print(Solution().isMatch('ab', '.*'))