from typing import List
class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    return True
        return False