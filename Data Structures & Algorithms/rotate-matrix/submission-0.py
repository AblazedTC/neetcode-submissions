class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        level = 0

        while level < len(matrix) // 2:
            for i in range(level, n - level):
                # Calculate TL, TR, BL, BR Positions
                TL = matrix[level][i]
                TR = matrix[i][n - level]
                BR = matrix[n - level][n - i]
                BL = matrix[n - i][level]

                # Rotate clockwise
                matrix[level][i] = BL
                matrix[i][n - level] = TL
                matrix[n - level][n - i] = TR
                matrix[n - i][level] = BR

            level += 1