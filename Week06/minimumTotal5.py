from typing import List
from six.moves import xrange
class Solution:
	def minimumTotal5(self,triangle):
		if not triangle:
			return
		res=triangle[-1]
		for i in xrange(len(triangle)-2,-1,-1):
			for j in xrange(len(triangle[i])):
				res[j]=min(res[j],res[j+1])+triangle[i][j]
		return res[0]
if __name__ == '__main__':
	triangle=[
			[2],
			[3,4],
			[6,5,7],
			[4,1,8,3]
	]
	solution=Solution()
	res=solution.minimumTotal5(triangle)
	print(res)
#空间复杂度：O(n) 自底向上 新开一个一维数组