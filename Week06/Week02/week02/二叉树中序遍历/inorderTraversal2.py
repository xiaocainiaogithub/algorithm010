from sklearn.tree import DecisionTreeClassifier
class Solution(object):
	def inorderTraversal(self,root):
		stack,rst=[root,],[]
		while stack:
			i=stack.pop()
			if isinstance(i,TreeNode):
				stack.extend([i.right,i.val,i.left])
			elif isinstance(i,int):
				rst.append(i)
		return rst