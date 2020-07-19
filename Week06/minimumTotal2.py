from typing import List
from six.moves import xrange
class Solution:
	def minimumTotal2(self,triangle):
		if not triangle:
			return
		res=[[0 for i in xrange(len(row))] for row in triangle]
		res[0][0]=triangle[0][0]
		for i in xrange(1,len(triangle)):
			for j in xrange(len(triangle[i])):
				if j==0:
					res[i][j]=res[i-1][j]+triangle[i][j]
				elif j==len(triangle[i])-1:
					res[i][j]=res[i-1][j-1]+triangle[i][j]
				else:
					res[i][j]=min(res[i-1][j-1],res[i-1][j])+triangle[i][j]
		return min(res[-1])
if __name__ == '__main__':
	triangle=[
			[2],
			[3,4],
			[6,5,7],
			[4,1,8,3]
	]
	solution=Solution()
	res=solution.minimumTotal2(triangle)
	print(res)
#空间复杂度：O(n^2/2) 自顶向下，开了一个res的空间