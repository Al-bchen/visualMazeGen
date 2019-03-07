# Different generator to generate the maze
import random
import time
import threading

from MazeData import MazeData, MazeBlockData, MazeBlockColor, MazeDirection

from PyQt5.QtWidgets import QWidget

class MazeGenerator():
	def __init__(self):
		super(MazeGenerator,self).__init__()
		self.mazeData = MazeData()
		self.widget = QWidget()

		self.flag_stopGenerator = False	# Require to stop generator immediately, used before running a new generator
		self.flag_skipPrinting = False	# Require to display final result immediately, not showing intermediate result
		self.lock_startGenerator = threading.Lock()		# Limit that at most one generator is active
		self.generatorMappingList = [self.generator_RecursiveBacktracking,
									 self.generator_Kruskal,
									 self.generator_Prim]	#Map index to generator

	def setMaze(self, x: MazeData):
		self.mazeData = x	#shallow copy

	def setWidget(self, x: QWidget):
		self.widget = x

	def resetMaze(self, index: int):
		if index < 10:
			self.mazeData.initMaze_grey()
		else:
			self.mazeData.initMaze_white()
		self.widget.update()

	def displayUpdate(self):
		if self.flag_stopGenerator == False and self.flag_skipPrinting == False:
			time.sleep(0.005)
			self.widget.update()

	def generatorCreateAndRun(self, index: int, size: int):
		self.flag_stopGenerator = True

		with self.lock_startGenerator: #Maxinum one active generator is allowed
			#use with, it automatically acquire() at beginning and release() at the end
			self.flag_stopGenerator = False
			self.mazeData.size = size
			self.resetMaze(index)
			time.sleep(1)

			self.generatorMappingList[index]()	# Call function by index
			# if index == 0:
			# 	self.generator_RecursiveBacktracking()
			# elif index == 1:
			# 	self.generator_Kruskal()
			# elif index == 2:
			# 	self.generator_Prim()
			# else:
			# 	self.generator_Test()

	def generator_Test(self):
		self.mazeData.initMaze()
		self.mazeData.block[1][1].color = MazeBlockColor.white
		self.mazeData.block[2][2].border['r'] = True
		self.widget.update()

	def generator_RecursiveBacktracking(self):
		def recursive_helper(x,y,px,py):	# Helper function for depth first search
			#grey: not visited / cyan: is visiting / dark cyan: the exact one is visiting / white: already visited
			if self.flag_stopGenerator == True:
				return

			randomDeltaList = MazeDirection.deltaList()
			random.shuffle(randomDeltaList)		# randomize direction selection

			self.mazeData.block[x][y].color = MazeBlockColor.darkcyan
			self.displayUpdate()
			self.mazeData.block[x][y].color = MazeBlockColor.cyan	# set vertex to visiting state
			for (dir,(dx,dy)) in randomDeltaList:
				nx = x + dx
				ny = y + dy
				if px == nx and py == ny:	# new vertex is parent vertex
					continue
				if nx < 0 or nx >= self.mazeData.size or ny < 0 or ny >=self.mazeData.size:	# new vertex is out of bound
					continue
				if self.mazeData.block[nx][ny].color != MazeBlockColor.grey:	# new vertex is already visited
					continue
				self.mazeData.block[x][y].border[dir] = False
				self.mazeData.block[nx][ny].border[MazeDirection.oppositeDirDict()[dir]] = False
				recursive_helper(nx, ny, x, y)	# add edge to maze and visit new vertex

			self.mazeData.block[x][y].color = MazeBlockColor.white	# set vertex to fully visited state
			self.displayUpdate()

		recursive_helper(0,0,-1,-1)
		self.displayUpdate()

	def generator_Kruskal(self):
		parentNode = [i for i in range(self.mazeData.size ** 2)]	#disjoint set, state of (x,y) saves to index (x + y * size)
		def findSetNum(x):	#findSet for disjoint set
			if parentNode[x] != x:
				parentNode[x] = findSetNum(parentNode[x])
			return parentNode[x]

		deltaDict = MazeDirection.deltaDict_twoDir()
		allEdges = []
		for x in range(self.mazeData.size):
			for y in range(self.mazeData.size):
				allEdges = allEdges + [((x,y), each[0]) for each in deltaDict]	#e.g. [((0,0),'d'),((0,0),'r'),((0,1),'d'), ...]

		random.shuffle(allEdges)	#Shuffle it, randomize selection

		for ((x1,y1),dir) in allEdges:
			if self.flag_stopGenerator == True:
				break
			x2 = x1 + deltaDict[dir][0]
			y2 = y1 + deltaDict[dir][1]

			if x2 < 0 or x2 >= self.mazeData.size or y2 < 0 or y2 >= self.mazeData.size:
				continue

			set1 = findSetNum(x1 + y1 * self.mazeData.size)
			set2 = findSetNum(x2 + y2 * self.mazeData.size)
			if set1 == set2:
				continue
			parentNode[set1] = set2

			self.mazeData.block[x1][y1].color = MazeBlockColor.white
			self.mazeData.block[x1][y1].border[dir] = False
			self.mazeData.block[x2][y2].color = MazeBlockColor.white
			self.mazeData.block[x2][y2].border[MazeDirection.oppositeDirDict()[dir]] = False
			self.displayUpdate()

	def generator_Prim(self):
		adjacentVerticeSet = {(0,0)}
		randomDeltaList = MazeDirection.deltaList()

		while adjacentVerticeSet:	# set not empty
			if self.flag_stopGenerator == True:
				break

			(x,y) = random.sample(adjacentVerticeSet, 1)[0]
			adjacentVerticeSet.remove((x,y))	# random select one vertex and remove it

			random.shuffle(randomDeltaList)		# randomize direction selection
			for (dir, (dx,dy)) in randomDeltaList:
				px = x + dx
				py = y + dy
				if px < 0 or px >= self.mazeData.size or py < 0 or py >=self.mazeData.size:	# new vertex is out of bound
					continue
				if self.mazeData.block[x][y].color != MazeBlockColor.white:
					break

			if self.mazeData.block[x][y].color == MazeBlockColor.white:
				continue


			self.displayUpdate()


