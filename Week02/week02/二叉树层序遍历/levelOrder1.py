from sklearn.tree import DecisionTreeClassifier
class Solution(object):
	def levelOrder1(self,root:'root'):
		if root is None:
			return []
		result = []
		previous_layer=[root]
		while previous_layer:
			current_layer=[]
			result.append([])
			for node in previous_layer:
				result[-1].append(node.val)
				current_layer.extend(node.children)
			previous_layer=current_layer
		return result