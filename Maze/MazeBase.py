class MazeBlockColor():
	white = '#ffffff'
	black = '#000000'
	grey = '#c0c0c0'
	cyan = '#00ffff'
	darkcyan = '#008080'

class MazeBlockData():
	def __init__(self):
		# Border / Edge
		self.border = dict()
		self.border['u'] = self.border['d'] = self.border['l'] = self.border['r'] = False

		# Color
		self.color = MazeBlockColor.white

		# Text
		self.text = ''

class MazeDirection():
	@staticmethod
	def deltaList():
		return [('u',(0,-1)), ('d',(0,1)), ('l',(-1,0)), ('r',(1,0))]
	@staticmethod
	def deltaDict():
		return dict(MazeDirection.deltaList())
	@staticmethod
	def oppositeDirDict():
		return {'u':'d', 'd':'u', 'l':'r', 'r':'l'}
	@staticmethod
	def deltaList_twoDir():
		return [('d',(0,1)), ('r',(1,0))]
	@staticmethod
	def deltaDict_twoDir():
		return dict(MazeDirection.deltaList_twoDir())

class MazeData():
	def __init__(self):
		self.size = 30
		self.initMaze()

	def initMaze(self):
		self.initMaze_grey()

	def initMaze_grey(self):
		self.block = [[MazeBlockData() for i in range(self.size)] for j in range(self.size)]
		for x in range(self.size):
			for y in range(self.size):
				self.block[x][y].color = MazeBlockColor.grey
				self.block[x][y].border['u'] \
					= self.block[x][y].border['d'] \
					= self.block[x][y].border['l'] \
					= self.block[x][y].border['r'] = True

	def initMaze_white(self):
		self.block = [[MazeBlockData() for i in range(self.size)] for j in range(self.size)]
		for i in range(self.size):
			self.block[i][0].border['u'] = True
			self.block[i][self.size - 1].border['d'] = True
			self.block[0][i].border['l'] = True
			self.block[self.size - 1][i].border['r'] = True
