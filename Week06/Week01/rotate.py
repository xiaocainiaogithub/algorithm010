class Solution(object):
	def rotate(self, nums):
		len = nums.length
		k = k % len
		count = 0
		start = 0
		for count in range(0,len):
			cur = start
			pre = nums[cur]
			while(start != cur):
				next = (cur + k) % len
				temp = nums[next]
				nums[next] = pre
				pre = temp
				cur = next
				count=count+1
			start=start+1