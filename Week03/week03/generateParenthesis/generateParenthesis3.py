class Solution(object):
	def generateParenthesis3(self,n,open=0):
		if n>0<=open:
			return['('+p for p in self.generateParenthesis3(n-1,open+1)]+\
				[')'+p for p in self.generateParenthesis3(n,open-1)]
		return[')'*open]*(not n)