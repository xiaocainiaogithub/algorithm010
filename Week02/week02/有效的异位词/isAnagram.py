class Solution:
	def isAnagramHash(self, s: str, t: str) -> bool:
		if len(s)!=len(t):
			return False
		if sorted(s)!=sorted(t):
			return False
		return Ture