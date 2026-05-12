from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = Counter(s1)
        window = Counter(s2[:len(s1)])

        l, r = 0, len(s1)

        while r < len(s2):
            if window == freq:
                return True

            # add right char
            window[s2[r]] = window.get(s2[r], 0) + 1

            # remove left char
            if window[s2[l]] == 1:
                window.pop(s2[l])
            else:
                window[s2[l]] -= 1

            l += 1
            r += 1

        return window == freq