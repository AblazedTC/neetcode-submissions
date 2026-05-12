class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = {}
        maxLen = 0

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen