from typing import List
class Solution:
	def minimumTotal1(self,triangle:List[List[int]])->int:
		dp=triangle #初始化，将数组全部装入dp
		for i in range(len(triangle)-2,-1,-1):
			for j in range(len(triangle[i])):
				dp[i][j]+=min(dp[i+1][j],dp[i+1][j+1])
		return triangle[0][0]
if __name__ == '__main__':
	triangle=[
			[2],
			[3,4],
			[6,5,7],
			[4,1,8,3]
	]
	solution=Solution()
	res=solution.minimumTotal1(triangle)
	print(res)