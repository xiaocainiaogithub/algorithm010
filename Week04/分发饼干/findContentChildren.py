from typing import List
class Solution:
	def findContentChildren(self,g:List[int],s:List[int])->int:
		res=0
		g.sort()
		s.sort()
		g_length=len(g)
		s_length=len(s)
		i=0
		j=0
		while i<g_length and j<s_length:
			if g[i]<=s[j]:
				res+=1
				i+=1
				j+=1
			else:
				j+=1
		return res
if __name__ == '__main__':
	g=[1,2,3]
	s=[1,1]
	solution=Solution()
	result=solution.findContentChildren(g,s)
	print(result)