解码方法：
解法1：
class Solution:
    def numDecoding1(self,s:str)->int:
        n = len(s)
        if n == 0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 #只有一个数的时候肯定为1
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[-1] += dp[-2]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[-1] += dp[-3]
                dp.pop(0)
        return dp[-1]
if __name__ == '__main__':
    s="226"
    solution=Solution()
    res=solution.numDecoding1(s)
    print(res)
#执行时间：40ms,83.52%,内耗13.6mb,6.25%

解法2：
class Solution:
    def numDecoding2(self,s:str)->int:
        pp, p = 1,int(s[0] !='0')
        for i in range(1,len(s)):
            pp , p = p, pp * (9 < int(s[i-1 : i+1]) <= 26) + p * (int(s[i]) > 0)
        return p
if __name__ == '__main__':
    s="226"
    solution=Solution()
    res=solution.numDecoding2(s)
    print(res)
#动态规划：执行时间：48ms,38.50%;内耗13.8mb,6.25%