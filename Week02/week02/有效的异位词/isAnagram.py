class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s)!=len(t):
			return False
		if sorted(s)!=sorted(t):
			return False
		return True
if __name__ == '__main__':
	s="anagram"
	t="nagaram"
	solution=Solution()
	result=solution.isAnagram(s,t)
	print(result)