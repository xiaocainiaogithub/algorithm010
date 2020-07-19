from typing import List
class Solution(object):
	def rotate(self, nums:List[int],k:int)->List[int]:
		len1 = len(nums)
		k = k % len1
		for i in range(k):
			nums.insert(0,nums.pop())
		return nums
if __name__ == '__main__':
	nums=[1,2,3,4,5,6,7]
	k=3
	solution=Solution()
	result=solution.rotate(nums,k)
	print(result)