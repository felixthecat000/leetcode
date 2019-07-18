class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def parse_char(s_remainder, char, star=False):
            """
            Match only the current character.
            Returns unmatched part of s if successful or None if match incorrect.
            """
            
            # set match char if wild card
            if char == '.':
                #if len(s_remainder) > 1 and star:
                #    s_remainder = s_remainder[1:]
                char = s_remainder[0]

            if s_remainder[0] != char:
                if star:
                    return s_remainder
                else:
                    raise Exception('No Match')

            # if in 'star' mode get run of same characters
            i = 1
            if star:
                while (len(s_remainder) > i and (s_remainder[i] == s_remainder[0])):
                    i += 1

            return s_remainder[i:]

        def select_char(pattern):
            
            # check for star
            if len(pattern) > 1:
                if pattern[1] == '*':
                    return pattern[0], True, pattern[2:]
            
            # otherwise return standard match
            return pattern[0], False, pattern[1:]

        while len(s) > 0 or len(p) > 0:
            # TODO: put char into memory, reuse if fails
            char, star, p = select_char(p)
            s = parse_char(s, char, star)
            return True
        except:
            return False

print(Solution().isMatch('ab', '.*'))