class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 1

        longestSub = 1

        seen = set(s[i])
        while i < len(s) and j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                seen.remove(s[i])
                i += 1
            longestSub = max(longestSub, j - i)

        return longestSub
