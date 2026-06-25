class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        ans = []

        startPart = 0
        endPart = 0

        for i in range(len(s)):
            if s[i] in freq:
                endPart += freq[s[i]]
                freq.pop(s[i])

            if i + 1 == endPart:
                ans.append(endPart - startPart)
                startPart = endPart

        return ans