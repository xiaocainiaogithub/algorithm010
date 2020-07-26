第七周学习笔记：
字典树（trie）：
字典树，即trie树，又称为单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎用于文本词频统计。
它的优点是：最大限度地减少无畏的字符串比较，查询效率比哈希表高。
基本性质：
1、结点本身不存完整单词；
2、从根节点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串；
3、每个结点的所有子结点路径代表的字符都不相同。
trie树的核心思想：空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
class Trie(object):
	def__int__(self):
		self.root={}
		self.end_of_word="#"
	def insert(self,word):
		node=self.root
		for char in word:
			node=node.setdefault(char,{})
		node[self.end_of_word]=self.end_of_word
	def search(self,word):
		node=self.root
		for char in word:
			if char not in node:
				return False
			node=node[char]
		return self.end_of_word in node
	def startsWith(self,prefix):
		node=self.root
		for char in prefix:
			if char not in node:
				return False
			node=node[char]
		return True

trie树代码模板：
dx=[-1,1,0,0]
dy=[0,0,-1,1]
END_OF_WORD="#"
class Solution(object):
	def findWords(self,board,words):
		if not board or not board[0]:return []
		if not word:return []
		self.result=set()
		#构建trie
		root=collections.defaultdict()
		for word in words:
			node=root
			for char in word:
				node=node.setdefault(char,collections.default())
			node[END_OF_WORD]=END_OF_WORD
		self.m,self.n=len(board),len(board[0])
		for i in xrange(self.m):
			for j in xrange(self.n):
				if board[i][j] in root:
					self._dfs(board,i,j,"",root)
		return list(self.result)
	def _dfs(self,board,i,j,cur_word,cur_dict):
		cur_word+=board[i][j]
		cur_dict=cur_dict[board[i][j]]
		if END_OF_WORD in cur_dict:
			self.result.add(cur_word)
		tmp,board[i][j]=board[i][j],'@'
		for k in xrange(4):
			x,y=i+dx[k],j+dy[k]
			if 0<=x<self.m and 0<=y<self.n and board[x][y] !='@' and board[x][y] in cur_dict:
		board[i][j]=tmp


并查集：
基本操作：
1、makeSet(s):建立一个新的并查集，其中包含s个单元素集合。
2、unionSet(x,y):把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并.
3、find(x):找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。
python实现：
def init(p):
	#for i =0...n:p[i]=i;
	p=[i for i in range(n)]
def union(self,p,i,j):
	p1=self.parent(p,i)
	p2=self.parent(p,j)
	p[p1]=p2
def parent(self,p,i):
	root=i
	while p[root] !=root:
		root=p[root]
	while p[i] !=i:#路径压缩
		x=i;i=p[i];p[x]=root
	return root

高级搜索：
初级搜索：
1、朴素搜索
2、优化方式：不重复（Fibonacci）、剪枝（生成括号问题）
3、搜索方向：
DFS:depth first search 深度优先搜索
BFS：breadth first search 广度优先搜索
双线搜索，启发式搜索

A*search 模板：
def AstarSearch(graph,start,end):
	pq=collections.priority_queue() #优先级->估价函数
	pq.append([start])
	visited.add(start)
	while pq:
		node=pq.pop()
		visited.add(node)
		process(node)
		nodes=generate_related_nodes(node)
		unvisited=[node for node in nodes if node not in visited]
		pq.push(unvisited)

估价函数：
启发式函数：h(n),它用来评价哪些结点最有希望的是一个我们要找的结点，h(n)会返回一个非负实数，也可以认为是从结点n的目标节点路径的估计成本。
启发式函数时一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。

AVL树和红黑树：
平衡二叉树：
保证性能的关键：
1、保证二维维度！ ->左右子树结点平衡（recusively）
2、balanced

AVL树：
1、发明者G.M.A的lson-Velsky 和 Evgenii Landis
2、Balance Factor(平衡因子):是它的左子树的高度减去它右子树的高度（有时相反），
balance factor={-1,0,1}
3、通过旋转操作来进行平衡（四种）：
（1）左旋
（2）右旋
（3）左右旋
（4）右左旋
AVL总结：
1、平衡二叉搜索树
2、每个节点存balance factor={-1,0,1}
3、四种旋转操作
不足：结点需要存储额外信息，且调整次数频繁（int型）

红黑树（red-black Tree）：
红黑树是一种近似平衡的二叉搜索树（Bianary Search Tree）,它能够确保任何一个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树：
1、每个结点要么是红色，要么是黑色
2、根结点是黑色
3、每个叶结点（NIL结点，空结点）是黑色的。
4、不能有相邻的两个红色结点
5、从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。