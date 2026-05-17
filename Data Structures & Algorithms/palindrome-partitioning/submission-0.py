class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curCombo = []

        def search(i: int, prevSplit: int):
            if i == len(s):
                if self.isPalindrome(s[prevSplit:i]):
                    curCombo.append(s[prevSplit:i])
                    ans.append(curCombo.copy())
                    curCombo.pop()
                return

            # Split here
            if self.isPalindrome(s[prevSplit:i]):
                curCombo.append(s[prevSplit:i])
                search(i + 1, i)
                curCombo.pop()

            # Don't split
            search(i + 1, prevSplit)

        search(1, 0)
        return ans

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]