from sklearn.tree import DecisionTreeClassifier
class Solution(object):
	def preorderTraversal3(self,root):
		'''
		:type root:Treenode
		:rtype:List[int]
		'''
		node,output=root,[]
		while node:
			if not node.left:
				output.append(node.val)
				node=node.right
			else:
				predecessor=node.left
				while predecessor.right and predecessor.right is not node:
					predecessor=predecessor.right
				if not predecessor.right:
					output.append(node.val)
					predecessor.right=node
					node=node.left
				else:
					predecessor.right=None
					node=node.right
		return output