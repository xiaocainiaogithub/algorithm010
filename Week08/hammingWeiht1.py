class Solution:
	def hammingWeiht1(self,n:int)->int:
		n = bin(n)
		count = 0
		for c in n:
			if c == '1':
				count += 1
		return count
if __name__ == '__main__':
	n = 0o10000000000000000000000000001011 #不允许十进制整数文本中的前导零；需使用0o前缀
	solution=Solution()
	res=solution.hammingWeiht1(n)
	print(res)
#执行时间：44ms,51.99%;内耗13.8mb,10.10%