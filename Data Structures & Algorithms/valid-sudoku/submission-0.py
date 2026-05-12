class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowTable = {i: set() for i in range(9)}
        colTable = {i: set() for i in range(9)}
        sqTable = {i: set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                tableCalc = (r // 3) * 3 + (c // 3)

                if num in rowTable[r] or num in colTable[c] or num in sqTable[tableCalc]:
                    return False

                rowTable[r].add(num)
                colTable[c].add(num)
                sqTable[tableCalc].add(num)

        return True