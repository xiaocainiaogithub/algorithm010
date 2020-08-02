from typing import List
class Solution:
	def merge(self, intervals:List[List[int]])->List[List[int]]:
		intervals.sort(key = lambda x:x[0])
		merged = []
		for interval in intervals:
			#如果列表为空，或者当前区间与上一区间不重合，直接添加
			if not merged or merged[-1][1] < interval[0]:
				merged.append(interval)
			else:
				#否则的话，我们就可以与上一区间进行合并
				merged[-1][1] = max(merged[-1][1], interval[1])
		return merged

if __name__ == '__main__':
	intervals=[[1,3],[2,6],[8,10],[15,18]]
	solution=Solution()
	res=solution.merge(intervals)
	print(res)
#执行时间：52ms,65.12%;内耗14.6mb,60.61%
#时间复杂度：O(nlogn)，其中n为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlogn)。
#空间复杂度：O(logn)，其中n为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(logn)即为排序所需要的空间复杂度。
