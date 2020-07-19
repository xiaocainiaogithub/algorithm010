from sklearn.tree import DecisionTreeClassifier
class Solution(object):
	def levelOrder(self,root:'Node'):
		if root is None:
			return []
		result=[]
		queue=collections.deque([root])
		while queue:
			level=[]
			for _ in range(len(queue)):
				node=queue.popleft()
				level.append(node.val)
				queue.extend(node.children)
			result.append(level)
		return result