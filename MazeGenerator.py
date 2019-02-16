import random
import time
import threading

from MazeData import MazeData, MazeBlockData, MazeBlockColor

from PyQt5.QtWidgets import QWidget

class MazeGenerator():
	def __init__(self):
		super(MazeGenerator,self).__init__()
		self.mazeData = MazeData()
		self.widget = QWidget()

		# 0: not active/ 1: running/ 2: require to stop
		self.generatorStopFlag = False
		self.lock_setGeneratorStopFlag = threading.Lock()
		self.lock_startGenerator = threading.Lock()

	def setMaze(self, x):
		self.mazeData = x	#shallow copy
	def setWidget(self, x):
		self.widget = x

	def resetMaze(self, index):
		if index < 10:
			self.mazeData.initMaze_grey()
		else:
			self.mazeData.initMaze_white()
		self.widget.update()

	def displayUpdate(self):
		if self.generatorStopFlag == False:
			time.sleep(0.004)
			self.widget.update()

	def generator_selector(self, index, size):

		with self.lock_setGeneratorStopFlag:
			self.generatorStopFlag = True

		# self.lock_setGeneratorStopFlag.acquire()
		# self.generatorStopFlag = True
		# self.lock_setGeneratorStopFlag.release()

		with self.lock_startGenerator: #Maxinum one active generator is allowed
			# self.lock_startGenerator.acquire()
			self.generatorStopFlag = False
			self.mazeData.size = size
			self.resetMaze(index)
			time.sleep(1)
			if index == 0:
				self.generator_RecursiveBacktracking()
			elif index == 1:
				self.generator_Kruskal()
			elif index == 2:
				self.generator_Prim()
			else:
				self.generator_Test()
			# self.lock_startGenerator.release()

	def generator_Test(self):
		self.mazeData.initMaze()
		self.mazeData.block[1][1].color = MazeBlockColor.white
		self.mazeData.block[2][2].border['r'] = True
		self.widget.update()

	def generator_RecursiveBacktracking(self):
		def recursive_helper(x,y,px,py):
			#black: not visited
			#cyan: is visiting
			#white: already visited
			if self.generatorStopFlag == True:
				return

			randomMappingList = MazeBlockData.mappingList()
			random.shuffle(randomMappingList)

			self.mazeData.block[x][y].color = MazeBlockColor.darkcyan
			self.displayUpdate()
			self.mazeData.block[x][y].color = MazeBlockColor.cyan
			for each in randomMappingList:
				nx = x+each[1][0]
				ny = y+each[1][1]
				if px == nx and py == ny:
					continue
				if nx < 0 or nx >= self.mazeData.size or ny < 0 or ny >=self.mazeData.size:
					continue
				if self.mazeData.block[nx][ny].color != MazeBlockColor.grey and self.mazeData.block[nx][ny].border[MazeBlockData.oppositeDirection()[each[0]]] == True:
					continue
				self.mazeData.block[x][y].border[each[0]] = False
				self.mazeData.block[nx][ny].border[MazeBlockData.oppositeDirection()[each[0]]] = False
				recursive_helper(nx, ny, x, y)

			self.mazeData.block[x][y].color = MazeBlockColor.white
			self.displayUpdate()

		recursive_helper(0,0,-1,-1)
		self.displayUpdate()

	def generator_Kruskal(self):
		parentNode = [i for i in range(self.mazeData.size ** 2)]	#disjoint set
		def findSetNum(x):
			if parentNode[x] != x:
				parentNode[x] = findSetNum(parentNode[x])
			return parentNode[x]

		mappingDict = dict(MazeBlockData.mappingList_noDuplicate())
		allEdges = []
		for x in range(self.mazeData.size):
			for y in range(self.mazeData.size):
				allEdges = allEdges + [((x,y), each[0]) for each in mappingDict]

		random.shuffle(allEdges)

		for e in allEdges:
			if self.generatorStopFlag == True:
				break
			x1 = e[0][0]
			y1 = e[0][1]
			x2 = e[0][0] + mappingDict[e[1]][0]
			y2 = e[0][1] + mappingDict[e[1]][1]

			if x2 < 0 or x2 >= self.mazeData.size or y2 < 0 or y2 >= self.mazeData.size:
				continue

			set1 = findSetNum(x1 + y1 * self.mazeData.size)
			set2 = findSetNum(x2 + y2 * self.mazeData.size)
			if set1 == set2:
				continue
			parentNode[set1] = set2

			self.mazeData.block[x1][y1].color = MazeBlockColor.white
			self.mazeData.block[x1][y1].border[e[1]] = False
			self.mazeData.block[x2][y2].color = MazeBlockColor.white
			self.mazeData.block[x2][y2].border[MazeBlockData.oppositeDirection()[e[1]]] = False
			self.displayUpdate()

	def generator_Prim(self):
		mappingDict = MazeBlockData.mappingDict()
		mappingList = MazeBlockData.mappingList()
		adjacentVertice = [(0,0)]
		adjacentVerticeDir = {(0,0): ''}

		while len(adjacentVertice) > 0:
			if self.generatorStopFlag == True:
				break

			random.shuffle(adjacentVertice)
			(x,y) = adjacentVertice.pop()
			d = adjacentVerticeDir[(x,y)]
			if self.mazeData.block[x][y].color == MazeBlockColor.white:
				continue

			self.mazeData.block[x][y].color = MazeBlockColor.white
			if d != '':
				px = x + mappingDict[d][0]
				py = y + mappingDict[d][1]
				self.mazeData.block[x][y].border[d] = False
				self.mazeData.block[px][py].border[MazeBlockData.oppositeDirection()[d]] = False

			for each in mappingList:
				nx = x + each[1][0]
				ny = y + each[1][1]
				if nx < 0 or nx >= self.mazeData.size or ny < 0 or ny >=self.mazeData.size:
					continue
				if self.mazeData.block[nx][ny].color == MazeBlockColor.white:
					continue
				elif self.mazeData.block[nx][ny].color == MazeBlockColor.cyan:
					if random.choice([True,False]) == True:
						adjacentVerticeDir[(nx,ny)] = MazeBlockData.oppositeDirection()[each[0]]
				elif self.mazeData.block[nx][ny].color == MazeBlockColor.grey:
					self.mazeData.block[nx][ny].color = MazeBlockColor.cyan
					adjacentVertice.append((nx,ny))
					adjacentVerticeDir[(nx,ny)] = MazeBlockData.oppositeDirection()[each[0]]

			self.displayUpdate()


