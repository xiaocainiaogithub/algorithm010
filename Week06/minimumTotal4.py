from typing import List
from six.moves import xrange
class Solution:
	def minimumTotal4(self,triangle):
		if not triangle:
			return
		for i in xrange(len(triangle)-2,-1,-1):
			for j in xrange(len(triangle[i])):
				triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
		return triangle[0][0]
if __name__ == '__main__':
	triangle=[
			[2],
			[3,4],
			[6,5,7],
			[4,1,8,3]
	]
	solution=Solution()
	res=solution.minimumTotal4(triangle)
	print(res)
#自底向上走