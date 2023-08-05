from typing import List
import numpy as np

class Solution:
    # O(m * log(n) + n * log(m))  too slow
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] == target:
            return True
        if matrix[0][0] != target and len(matrix) == 1 and len(matrix[0]) == 1:
            return False
        matrix = np.array(matrix)
        x1, y1, x2, y2 = 0, 0, len(matrix[0])-1, len(matrix)-1

        while not (x1>=x2 and y1>=y2):
            top = self.bsearch(matrix[y1], x1, x2, target)
            if top=="t":
                return True
            x2 = top
            print("x2: %d" % x2)

            right = self.bsearch(matrix[:, x2], y1, y2, target)
            if right=="t":
                return True
            y1 = right + 1
            if y1>y2:
                return False
            print("y1: %d" % y1)

            bottom = self.bsearch(matrix[y2], x1, x2, target)
            if bottom=="t":
                return True
            x1 = bottom + 1
            if x1>x2:
                return False
            print("x1: %d" % x1)

            left = self.bsearch(matrix[:, x1], y1, y2, target)
            if left=="t":
                return True
            y2 = left
            print("y2: %d" % y2)
        
        return False
    
    def bsearch(self, arr, left, right, target):
            print(arr)
            print(target)
            max_index = -1
            while left <= right:
                mid = left + (right-left)//2
                print("left: %d, right: %d, value: %d" % (left, right, arr[mid]))
                if arr[mid] == target:
                    return "t"
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    max_index = mid
                    left = mid + 1
            return max_index
    
s = Solution()
ret = s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
print(ret)

# class Solution:
#     # O (m+n)
#     def searchMatrix(self, matrix, target):
#         if not matrix or not matrix[0]:
#             return False

#         rows, cols = len(matrix), len(matrix[0])
#         x, y = cols - 1, 0

#         while x >= 0 and y < rows:
#             if matrix[y][x] == target:
#                 return True
#             elif matrix[y][x] > target:
#                 x -= 1
#             else:
#                 y += 1

#         return False