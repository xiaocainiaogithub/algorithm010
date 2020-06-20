#from pytreelib import BinaryTreeNode
from sklearn.tree import DecisionTreeClassifier
class Soulution(object):
	def inorderTraversal(self,root):
		WHITE,GRAY=0,1
		res=[]
		stack=[WHITE,GRAY]
		while stack:
			color,node=stack.pop()
			if node is None:
				continue
			if color==WHITE:
				stack.append((WHITE,node.right))
				stack.append((GRAY,node))
				stack.append((WHITE,node.left))
			else:
				res.append(node.val)
		return res
