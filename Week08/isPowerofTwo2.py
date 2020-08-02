class Solution:
	def isPowerofTwo2(self,n:int)->bool:
		if n == 0:
			return False
		return n & (-n) == n
if __name__ == '__main__':
	n = 1
	solution=Solution()
	res=solution.isPowerofTwo2(n)
	print(res)
#位运算(获取二进制中最右边的1)：执行时间：40ms,8356.%;内耗13.7mb,25.48%
#时间复杂度：O(1)。
#空间复杂度：O(1)。