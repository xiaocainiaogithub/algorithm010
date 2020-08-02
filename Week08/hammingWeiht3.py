class Solution:
	def hammingWeiht3(self,n:int)->int:
		count = 0
		while n:
			res = n % 2
			if res == 1:
				count += 1
			n //= 2
		return count
if __name__ == '__main__':
	n = 0o10000000000000000000000000001011 #不允许十进制整数文本中的前导零；需使用0o前缀
	solution=Solution()
	res=solution.hammingWeiht3(n)
	print(res)
#执行时间：40ms,76.32%;内耗13.7mb,24.52%