from sklearn.tree import DecisionTreeClassifier
class Solution(object):
	def preorderTraversal1 (self,root):
		WHITE,GRAY=0,1
		res=[]
		Stack=[WHITE,GRAY]
		while Stack:
			color,Node=Stack.pop()
			if Node==null:
				continue
			if color==WHITE:
				Stack.append((WHITE,node.right))
				Stack.append((WHITE,node.left))
				Stack.append((GRAY,node))
			else:
				Stack.append(node.val)
		return res

