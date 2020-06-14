class removeDuplicates:
    def removeDuplicates(self, nums):
    	'''
    	:type nums:list[int]
    	:rtype:int
    	'''
    	if not nums or nums.length == 0:
    		return 0
    	p = 0
    	q = 1
    	while(q < nums.length):
    		if(nums[p] != nums[q]):
    			if(q - p > 1):
    				nums[p + 1] = nums[q]
    			p=p+1
    		q=q+1
    	return p + 1