from typing import List
class Solution:
	directions=[(-1,0),(0,-1),(1,0),(0,1)]
	def numIslands1(self,grid:List[List[str]])->int:
		m=len(grid)
		if m==0:
			return 0
		n=len(grid[0])
		maked=[[False for _ in range(n)] for _ in range(m)]
		count=0
		for i in range(m):
			for j in range(n):
				if not maked[i][j] and grid[i][j]=='1':
					count+=1
					self.__dfs(grid,i,j,m,n,maked)
		return count
	def __dfs(self,grid,i,j,m,n,maked):
		maked[i][j]=True
		for direction in self.directions:
			new_i = i+direction[0]
			new_j = j+direction[1]
			if 0<=new_i<m and 0<=new_j<n and not maked[new_i][new_j] and grid[new_i][new_j]=='1':
				self.__dfs(grid,new_i,new_j,m,n,maked)
if __name__=='__main__':
	grid=[['1','1','1','1','0'],
		['1','1','0','1','0'],
		['1','1','0','0','0'],
		['0','0','0','0','0']]
	solution=Solution()
	result=solution.numIslands(grid)
	print(result)

