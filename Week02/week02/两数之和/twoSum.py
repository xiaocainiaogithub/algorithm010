class Solution:
	def twoSum(self,target):
		lens=lens(nums)
		j=-1
		for i in range(lens):
			if(nums.count(target-nums[i])==1)&&(target-nums[i]==nums[i])
				continue
			else:
				j=nums.index(target-nums[i],i+1)
				break
		if j>0:
			return [i,j]
		else:
			return []