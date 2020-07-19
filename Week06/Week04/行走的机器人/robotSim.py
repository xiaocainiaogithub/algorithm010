from six.moves import xrange
class Solution:
	def robotSim(self,commands,obstacles):
		dx=[0,1,0,-1]
		dy=[1,0,-1,0]
		x=y=di=0
		obstacleSet=set(map(tuple,obstacles))
		ans=0

		for cmd in commands:
			if cmd==-2:
				di=(di-1)%4
			elif cmd==-1:
				di=(di+1)%4
			else:
				for k in xrange(cmd):
					if (x+dx[di],y+dy[di]) not in obstacleSet:
						x+=dx[di]
						y+=dy[di]
						ans=max(ans,x*x+y*y)
		return ans

if __name__ == '__main__':
	commands=[4,-1,4,-2,4]
	obstacles=[[2,4]]
	solution=Solution()
	result=solution.robotSim(commands,obstacles)
	print(result)