class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(array, tar):
            low, high = 0, len(array)

            while low < high:
                mid = (low + high) // 2

                if array[mid] == tar:
                    return True

                if tar > array[mid]:
                    low = mid + 1
                else:
                    high = mid

            return False

        low, high = 0, len(matrix)

        while low < high:
            mid = (low + high) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return search(matrix[mid], target)

            if target > matrix[mid][-1]:
                low = mid + 1
            else:
                high = mid

        return False