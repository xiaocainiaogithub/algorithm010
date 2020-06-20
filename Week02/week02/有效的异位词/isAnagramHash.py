class Solution:
	def isAnagramHash(self, s: str, t: str) -> bool:
		if len(s)!=len(t):
			return False
		dicts=collection.defaultedict(int)
		for i in range(len(s)):
			dicts[s[i]]=dicts[s[i]]+1
			dicts[t[i]]=dicts[t[i]]-1
		for val in dicts.values():
			if val !=0:
				return False
		return Ture