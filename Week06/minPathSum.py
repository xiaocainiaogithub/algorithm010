from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if m==n==0:continue
                elif m==0: grid[m][n]=grid[m][n-1]+grid[m][n]
                elif n==0: grid[m][n]=grid[m-1][n]+grid[m][n]
                else: grid[m][n]=min(grid[m-1][n],grid[m][n-1])+grid[m][n]
        return grid[-1][-1]
if __name__ == '__main__':
	grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
	solution=Solution()
	res=solution.minPathSum(grid)
	print(res)