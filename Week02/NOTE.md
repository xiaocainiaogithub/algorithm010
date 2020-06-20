学习笔记
1、哈希表(Hash table):也叫做散列表，是根据关键码值(Key value)而直接进行访问的数据结构。它通过关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数(Hash Fuction)，存放记录的数组叫作哈希表(或散列表)。
当哈希值相同存放位置相同时，常采用拉链式解决冲突法。
真正工程上使用的是在哈希表抽象出来的，比较多的是Map和Set。Map对应Python是Dict/Dictionary/Json；Set对应Python是Set。

Map:key-value对，key不重复
	new HashMap()/new TreeMap()
	map.set(key,value)
	map.get(key)
	map.has(key)
	map.size()
	map.clear()

Set:不重复元素的集合
	new HashSet()/new TreeSet()
	set.add(value)
	set.delete(value)
	set.hash(value)

Python code

list_x=[1,2,3,4]
map_x={
	'jack':100,
	'张三':80,
	'selina':90,
	...
}

set_x={'jack','selina','Andy'}
set_y=set(['jack','selina','Andy'])

2、树（tree）、二叉树、二叉搜索树
linked list 是特殊化的Tree,Tree是特殊化的Graph
Python
class TreeNode:
	def__init__(self,val):
		self.val=val
		self.left,self.right=None,None

C++
struct TreeNode{
	int val;
	TreeNode*left;
	TreeNode*right;
	TreeNode(int x):val(x),left(NULL),right(NULL){}
}

Java
public class TreeNode{
	public int val;
	public TreeNode left,right;
	public TreeNode(int val){
		this.val=val;
		this.left=null;
		this.right=null;
	}
}

二叉树的遍历:
1、前序（Pre-order）：根-左-右
2、中序（In-order）：左-根-右
3、后序（Post-order）：左-右-根

def preorder(self,root):
	if root:
		self.traverse_path append(root.val)
		self.preorder(root.left)
		self.preorder(root.right)

def inorder(self,root):
	if root:
		self.inorder(root.left)
		self.traverse_path append(root.val)
		self.inorder(root.right)

def postorder(self,root):
	if root:
		self.postorder(root.left)
		self.postorder(root.right)
		self.traverse_path append(root.val)

二叉搜索树（Binary Search Tree）
二叉搜索树，也称二叉排序树、有序二叉树（Ordered Binary Tree）、排序二叉树（Sorted Binary Tree），是指一颗空树或者具有下列性质的二叉树：
1、左子树上所有节点的值均小于它的根节点的值；
2、右子树上所有节点的值均大于它的根节点的值；
3、以此类推：左、右子树也分别为二叉查找树（这就是重复性！）

中序遍历：升序排列


二叉搜索树常见操作O（log n）：
1、查询
2、插入新节点（创建）
3、删除


堆 Heap
Heap:可以迅速找到一堆数中的最大或者最小值的数据结构。
将根节点最大的堆叫做大顶堆或者大根堆，根节点最小的堆叫做小顶堆或者小根堆。常见的堆有二叉堆(二向堆)、斐波那契堆等。
假设是大顶堆，则常见操作（API）：
find-max:O(1)
delete-max:O(logN)
insert(create):O(logN) or O(1)


二叉堆性质：
通过完全二叉树来实现（注意：不是二叉搜索树）
二叉堆（大顶）它满足下列性质：
1、是一颗完全树
2、树种任意节点的值总是>=其子节点的值

二叉堆
根节点（顶堆元素）是：a[0]
1、索引为i的左孩子的索引是（2*i+1）
2、索引为i的右孩子的索引是（2*i+2）
3、索引为i的父节点的索引是floor((i-1)/2)

insert 插入操作(HeapifyUP函数)  O(logN)
1、新元素一律先插入到堆的尾部
2、依次向上调整整个堆的结构（一直到根即可）

Delete Max 删除堆顶操作(HeapifyDown函数)  O(logN)
1、将堆尾元素替换到顶部（即堆顶被替代删除掉）
2、依次从根部向下调整整个堆的结构（一直到堆尾即可）

注意：二叉堆是对（优先队列Priority Queue）的一种常见且简单的实现，但并不是最优的实现。

图的属性
Graph(V,E)
V-vertex:点
1、度-入度和出度
2、点与点之间：连通与否
E-edge:边
1、有向和无向（单行线）
2、权重（边长）

图的表示
1、邻接矩阵（Adjacency matrix）
2、邻接表（Adjacency list）

基于图的常见算法
DFS 递归  和树中的DFS最大的区别：visited=set()
DFS代码：
visited=set()#和树中的DFS的最大区别
def dfs(node,visited):
	if node in visited: # terminator
		# already visited
		return
	visited.add(node)

	#process current node here.
	...
	for next_node in node.children():
		if not next_node in visited:
			dfs(next_node,visited)
BFS代码：
def BFS(grapg,start,end):
	queue=[]
	queue.append([start])
	visited=set()#和树中的BFS的最大区别
	while queue:
		node=queue.pop()
		visited.add(node)
		process(node)
		nodes=generate_related_nodes(node)
		queue.push(nodes)

