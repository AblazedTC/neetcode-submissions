class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        curCombo = ""
        if not digits:
            return []


        def search(i):
            nonlocal curCombo
            if i == len(digits):
                ans.append(curCombo)
                return

            for c in phoneMap.get(digits[i]):
                curCombo += c
                search(i + 1)
                curCombo = curCombo[:-1]
        
        search(0)
        return ans
        