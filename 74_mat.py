from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   # O(log(mn))
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        row = 0
        while left < right:
            mid = left + (right - left + 1) // 2    # left == mid will lead to dead loop
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid
                row = left  # 避免右移错过目标行
            else:
                return True

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False

    def searchMatrix_(self, matrix: List[List[int]], target: int) -> bool:
        # 看作一维数组, O(log(mn))
        pass
