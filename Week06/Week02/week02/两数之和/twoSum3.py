class Solution:
	def twoSum3(self,target):
		hashmap={}
		for ind,num in enumerate(nums):
			if hashmap.get(target-num) is not None:
				return [i,hashmap.get(target-num)]
			hashmap[num]=i