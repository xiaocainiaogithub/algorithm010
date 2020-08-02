class Solution:
	def hammingWeiht4(self,n:int)->int:
		count = 0
		while n:
			count += n & 1
			n >>= 1
		return count
if __name__ == '__main__':
	n = 0o10000000000000000000000000001011 #不允许十进制整数文本中的前导零；需使用0o前缀
	solution=Solution()
	res=solution.hammingWeiht4(n)
	print(res)
#执行时间：44ms,51.99%;内耗13.6mb,71.63%