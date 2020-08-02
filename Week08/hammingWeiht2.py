class Solution:
	def hammingWeiht2(self,n:int)->int:
		return bin(n).count('1')
if __name__ == '__main__':
	n = 0o10000000000000000000000000001011 #不允许十进制整数文本中的前导零；需使用0o前缀
	solution=Solution()
	res=solution.hammingWeiht2(n)
	print(res)
#执行时间：32ms,97.59%;内耗13.6mb,80.29%