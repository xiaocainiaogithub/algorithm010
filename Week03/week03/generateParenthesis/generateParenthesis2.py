class Solution(object):
	def generateParenthesis2(self,n):
		def generate(p,left,right):
			if right>=left>=0:
				yeild p
			for q in generate(p+'(',left-1,right):yield q
			for q in generate(p+')',left,right-1):yield q
		return list(generate('',n,n))