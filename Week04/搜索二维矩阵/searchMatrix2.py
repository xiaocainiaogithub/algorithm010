from typing import List
class Solution:
	def searchMatrix2(self,matrix:List[List[int]],target:int)->bool:
		m=len(matrix)
		if m==0:
			return False
		n=len(matrix[0])

		left,right=0,m*n-1
		while left<=right:
			mid_idx=(left+right)//2
			mid_element=matrix[mid_idx//n][mid_idx%n]
			if target==mid_element:
				return True
			else:
				if target<mid_element:
					right=mid_idx-1
				else:
					left=mid_idx+1
		return False
