class Solution:
	def twoSum1(self,target):
		lens=lens(nums)
		j=-1
		for i in range(lens):
			temp=nums[:i]
			if(target-nums[i])in temp:
				j=temp.index(target-nums[i])
		if j>0:
			return [i,j]