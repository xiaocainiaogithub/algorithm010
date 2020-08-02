class Solution:
	def isPowerofTwo3(self,n:int)->bool:
		if n == 0:
			return False
		return n & (n - 1) == 0
if __name__ == '__main__':
	n = 1
	solution=Solution()
	res=solution.isPowerofTwo3(n)
	print(res)
#位运算(去除二进制中最右边的1)：执行时间：36ms,93.69%;内耗13.6mb,64.33%
#时间复杂度：O(1)。
#空间复杂度：O(1)。