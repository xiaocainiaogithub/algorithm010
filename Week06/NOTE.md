第六周笔记：
动态规划与分治的区别：
1、本质上没有区别（关键看有无最优的子结构）
2、共性：找到重复子问题
3、差异性：最优子结构，中途可以淘汰次优解


傻递归 时间复杂度：O（2^n）或O（logN）指数级
优化递归 时间复杂度可以降级 O（N）
简化例子：
#递归+记忆式搜索（自顶向下）
int fib(int n,int[] ,memo){#加上了memo进行缓存
	if (n<=1){
		return n; #原来的写法：if(n==0){return 0}  if(n==1){return 1}
	}
	if(memo[n]==0){
		memo[n]=fib(n-1)+fib(n-2);
	}
	return memo[n];
}

#与其用记忆式搜索，不如用for循环（自底向上）
F[n]=F[n-1]+F[n-2]
a[0]=0,a[1]=1
for(int i =2;i<=n;i++){
	a[i]=a[i-1]+a[i-2];
}

递归模板：
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed


# Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}


分治模板：
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states


  count the paths
  int countPaths(boolean[][]grid,int row,int col){
    if(!validSquare(grid,row,col)) return 0;
    if(isAtEnd(grid,row,col)) return 1;
    return countPaths(grid,row+1,col)+countPaths(grid,row,col+1);
  }

  状态转移方程（DP方程）
  opt[i,j]=opt[i+1,j]+opt[i,j+1]
  完整逻辑：
  if a[i,j]='空地'：
    opt[i,j]=opt[i+1,j]+opt[i,j+1]
  else:
    opt[i,j]=0

  动态规划关键点：
  1、最优子结构 opt[n]=best_of(opt[n-1],opt[n-2],...)
  2、储存中间状态：opt[i]
  3、递推公式（美其名曰：状态转移方式或者DP方程）
  Fib:opt[i]=opt[i-1]+opt[i-2]
  二维路径：opt[i,j]=opt[i+1][j]+opt[i][j+1](且判断a[i,j]是否空地)


  DP方程
  if S1!=S2[-1]:LCS[S1,S2]=MAX(LCS[S1-1,S2],LCS[S1,S2-1])
  if S1[-1]==S2[-1]:LCS[S1,S2]=LCS[S1-1,S2-1]+1