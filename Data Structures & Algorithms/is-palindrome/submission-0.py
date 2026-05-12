class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumeric = "".join(c for c in s if c.isalnum()).lower()
        return alphaNumeric == alphaNumeric[::-1]