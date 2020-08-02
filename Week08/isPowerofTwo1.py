class Solution:
	def isPowerofTwo1(self,n:int)->bool:
		if n == 0:
			return False
		while n % 2 ==0:
			n /= 2
		return n == 1
if __name__ == '__main__':
	n = 1
	solution=Solution()
	res=solution.isPowerofTwo1(n)
	print(res)
#执行时间：28ms,99.59%;内耗13.8mb,5.10%
#时间复杂度：O(logn)。