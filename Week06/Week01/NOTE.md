学习笔记

1、数组(Array)：时间复杂度O（1）

2、链表(Linked list)：包含单链表、双向链表、循环链表

	Array时间复杂度	linked-list时间复杂度
	prepend	O(1)		O(1)
	append	O(1)		O(1)
	lookup	O(1)		O(n)
	insert	O(n)		O(1)
	delete	O(n)		O(1)

3、跳表（Skip list）：只能用于链表元素有序的情况。所以跳表对标的是平衡树（AVL Tree）和二分查找，是一种插入/删除/搜索 都是O(log n）的数据结构。空间复杂度O（n）

4、栈（Stack）：先入后出；添加、删除为O（n）

5、队列(Queue)：先入先出；添加、删除为O（1）

6、优先队列（Priority Queue）：插入O（1）；取出O（log n）--按照元素的优先级取出；底层具体实现的数据机构较为多样和复杂：堆(heap)、bst、treap

7、双端队列（Duque）：两端都可以进出的queue;插入和删除都是O（1）的操作

作业：
1、分析Queue和Prority Queue源码
（1）Queue:父类Collection
			方法：添加add、选择offer、移出remove、获取并移除头元素poll、获取但不移除头元素peek、元素element
 (2)Priority Queue:父类AbstractQueue
 			方法：添加add、选择offer、移出remove、contains、toArray、iterator、clear、comparator、spliterator
 相同点：
 方法——add\offer\remove
 不同点：
 顺序——Priority Queue 含优先级