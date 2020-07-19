学习笔记
递归python代码模板：
def recursion(level,param1,param2,...):
	#recursion terminator 递归终结者，必写，否则陷入死循环
	if level > MAX_LEVEL:
	process_result
	return

	#process logic in current level处理当层逻辑
	process(level,data...)

	#drill down下探到下一层
	self.recursion(level+1,p1,...)

	#reverse the current level status if needed清理当前层

	递归java代码模板：
	public void recur(int level,int param){
		//terminator
		if(level>MAX_LEVEL){
			//process result
			return;
		}

		//process current logic
		process(level,param);

		//drill down
		recur(level:level+1,newParam);

		//restore current status
	}



	思维要点：
	1、抵制人肉递归
	2、找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
	3、数学归纳法思维


	