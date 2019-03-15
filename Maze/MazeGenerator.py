# Different generator to generate the maze
import random
import time
import threading
import copy

from Maze.MazeBase import *
from MazeDisplay import MazeDisplay

class MazeGenerator(object):
	def __init__(self):
		super(MazeGenerator,self).__init__()
		self.mazeData = MazeData()
		self.widget = MazeDisplay(None)

		self.flag_stopGen = False		# Require to stop generator immediately, used before running a new generator
		self.flag_skipGen = False		# Require to display final result immediately without showing intermediate result
		self.flag_stepGen = False		# Require step generation

		self.event_stepGen = threading.Event()
		self.lock_startGenerator = threading.Lock()		# Limit that at most one generator is active
		self.lock_modifyFlag_stopGenerator = threading.Lock()

		self.generatorMappingList = [
			self.generator_RecursiveBacktracking,
			self.generator_Kruskal,
			self.generator_Prim,
			self.generator_HuntAndKill,
			self.generator_RecursiveDivision
		] 	# Map index to generator

	def setMaze(self, x: MazeData):
		self.mazeData = x 	# shallow copy

	def setWidget(self, x: MazeDisplay):
		self.widget = x

	def resetMaze(self, index: int):
		if self.generatorMappingList[index] != self.generator_RecursiveDivision:
			self.mazeData.initMaze_grey()
		else:
			self.mazeData.initMaze_white()

	def isOutOfMaze(self, x, y):
		return x < 0 or x >= self.mazeData.size or y < 0 or y >= self.mazeData.size

	def displayUpdate(self):
		if not self.flag_stopGen and not self.flag_skipGen:
			time.sleep(0.01)
			self.widget.update()

	def finishGenerating(self):
		if not self.flag_stopGen:
			self.widget.update()		# require immediate repaint
			self.mazeData.isGenerated = True

	def generatorReset(self, index: int, size: int):
		with self.lock_modifyFlag_stopGenerator:
			if self.flag_stopGen:		# Limit that only one generator can run
				return
			self.flag_stopGen = True
			self.flag_stepGen = False
			self.event_stepGen.set()

		with self.lock_startGenerator:		# Maximum one active generator is allowed
			# use with, the lock automatically acquire() at beginning and release() at the end
			self.flag_stopGen = False
			self.flag_skipGen = False
			self.flag_stepGen = False
			self.event_stepGen.clear()
			with self.widget.lock_maze:
				self.mazeData.size = size
				self.resetMaze(index)

			self.displayUpdate()

	def generatorStep(self, index: int, size: int):
		if self.flag_stepGen:
			self.event_stepGen.set()
		else:
			self.event_stepGen.clear()
			self.flag_stepGen = True

	def generatorRun(self, index: int, size: int):
		with self.lock_startGenerator:
			self.mazeData.isReset = False
			self.generatorMappingList[index]()		# Call function by index
			self.finishGenerating()

	def generatorCreateAndRun(self, index: int, size: int):
		self.generatorReset(index, size)
		time.sleep(1)
		self.generatorRun(index, size)

	def stepCheckpoint(self):
		if self.flag_stepGen:
			self.event_stepGen.wait()
			self.event_stepGen.clear()

	def generator_RecursiveBacktracking(self):		# generator using DFS
		def recursivebacktracking_dfs_helper(x, y, px, py):		# Helper function for DFS recursive calls
			# grey: not visited / cyan: is visiting / dark cyan: the exact one is visiting / white: already visited
			if self.flag_stopGen:
				return

			randomDeltaList = MazeDirection.getDeltaList()
			random.shuffle(randomDeltaList)		# randomize direction selection

			self.mazeData.block[x][y].color = MazeBlockColor.dark_cyan		# set current vertex to exact visiting state
			self.displayUpdate()
			self.stepCheckpoint()
			self.mazeData.block[x][y].color = MazeBlockColor.cyan		# set vertex to visiting state
			for (dir, (dx,dy)) in randomDeltaList:
				nx = x + dx
				ny = y + dy
				if px == nx and py == ny:
					continue
				if self.isOutOfMaze(nx, ny):
					continue
				if self.mazeData.block[nx][ny].color != MazeBlockColor.grey:
					continue
				self.mazeData.block[x][y].border[dir] = False
				self.mazeData.block[nx][ny].border[MazeDirection.getOppositeDirDict()[dir]] = False		# Add edge by removing walls
				recursivebacktracking_dfs_helper(nx, ny, x, y)
				self.mazeData.block[x][y].color = MazeBlockColor.cyan		# set vertex to visiting state

			self.mazeData.block[x][y].color = MazeBlockColor.white		# set vertex to fully visited state
			if not self.isOutOfMaze(px, py):
				self.mazeData.block[px][py].color = MazeBlockColor.dark_cyan
			self.displayUpdate()
			self.stepCheckpoint()

		recursivebacktracking_dfs_helper(random.randint(0, self.mazeData.size-1),random.randint(0, self.mazeData.size-1), -1, -1)		# call at here

	def generator_Kruskal(self):		# generator using Kruskal's Algorithm with disjoint set
		parentNode = [i for i in range(self.mazeData.size ** 2)]		# disjoint set, state of (x,y) saves to index (x + y * size)

		def djs_find(x):		# find() for disjoint set
			if parentNode[x] != x:
				parentNode[x] = djs_find(parentNode[x])
			return parentNode[x]

		def djs_union(x, y):		# union() for disjoint set
			parentNode[djs_find(x)] = djs_find(y)

		allEdges = []
		deltaDict = MazeDirection.getDeltaDict_twoDir()
		for x in range(self.mazeData.size):
			for y in range(self.mazeData.size):
				allEdges = allEdges + [((x,y), each[0]) for each in deltaDict]		# e.g. [((0,0),'d'),((0,0),'r'),((0,1),'d'), ...]

		random.shuffle(allEdges)		# Shuffle it, randomize selection

		for ((x1, y1), dir) in allEdges:
			if self.flag_stopGen:
				break
			x2 = x1 + deltaDict[dir][0]
			y2 = y1 + deltaDict[dir][1]

			if self.isOutOfMaze(x2, y2):
				continue

			set1 = djs_find(x1 + y1 * self.mazeData.size)
			set2 = djs_find(x2 + y2 * self.mazeData.size)
			if set1 == set2:
				continue
			djs_union(set1, set2)

			self.mazeData.block[x1][y1].color = MazeBlockColor.white
			self.mazeData.block[x1][y1].border[dir] = False
			self.mazeData.block[x2][y2].color = MazeBlockColor.white
			self.mazeData.block[x2][y2].border[MazeDirection.getOppositeDirDict()[dir]] = False
			self.displayUpdate()
			self.stepCheckPoint()

	def generator_Prim(self):		# generator using Prim's Algorithm
		adjacentVerticesSet = {(random.randint(0, self.mazeData.size-1),random.randint(0, self.mazeData.size-1))}
		randomDeltaList = MazeDirection.getDeltaList()
		firstVertex = True

		while adjacentVerticesSet:		# set not empty
			if self.flag_stopGen:
				break

			(x, y) = random.sample(adjacentVerticesSet, 1)[0]
			adjacentVerticesSet.remove((x, y))		# random select one vertex and remove it

			random.shuffle(randomDeltaList)		# randomize direction selection
			if not firstVertex:
				for (dir, (dx, dy)) in randomDeltaList:
					px = x + dx
					py = y + dy
					if self.isOutOfMaze(px, py):
						continue
					if self.mazeData.block[px][py].color == MazeBlockColor.white:
						self.mazeData.block[x][y].border[dir] = False
						self.mazeData.block[px][py].border[MazeDirection.getOppositeDirDict()[dir]] = False
						break

			firstVertex = False
			self.mazeData.block[x][y].color = MazeBlockColor.white
			for (ndir, (ndx, ndy)) in MazeDirection.getDeltaList():
					nx = x + ndx
					ny = y + ndy
					if not self.isOutOfMaze(nx, ny) and self.mazeData.block[nx][ny].color != MazeBlockColor.white:
						self.mazeData.block[nx][ny].color = MazeBlockColor.cyan
						adjacentVerticesSet.add((nx, ny))

			self.displayUpdate()
			self.stepCheckPoint()

	def generator_HuntAndKill(self):		# generator using Hunt Ant Kill
		def huntandkill_iterate_helper(x, y):
			while True:
				if self.flag_stopGen:
					return

				randomDeltaList = MazeDirection.getDeltaList()
				random.shuffle(randomDeltaList)		# randomize direction selection

				self.mazeData.block[x][y].color = MazeBlockColor.dark_cyan		# set current vertex to exact visiting state
				self.displayUpdate()
				self.mazeData.block[x][y].color = MazeBlockColor.cyan		# set vertex to visiting state

				flag_deadend = True
				for (dir, (dx,dy)) in randomDeltaList:
					nx = x + dx
					ny = y + dy
					if self.isOutOfMaze(nx, ny):
						continue
					if self.mazeData.block[nx][ny].color != MazeBlockColor.grey:
						continue
					self.mazeData.block[x][y].border[dir] = False
					self.mazeData.block[nx][ny].border[MazeDirection.getOppositeDirDict()[dir]] = False		# Add edge by removing walls
					x = nx
					y = ny
					flag_deadend = False
					break

				if flag_deadend:
					break

			for x in range(self.mazeData.size):
				for y in range(self.mazeData.size):
					if self.mazeData.block[x][y].color == MazeBlockColor.cyan:
						self.mazeData.block[x][y].color = MazeBlockColor.white
			self.displayUpdate()

		def huntandkill_scan_and_add_adjacent():		# scan(hunt) for the first unvisited vertex and add edge with adjacent visited vertex
			ret = None
			for x in range(self.mazeData.size):
				if ret:
					break
				if self.flag_stopGen:
					return None
				saved_column = copy.deepcopy(self.mazeData.block[x])		# save state
				for y in range(self.mazeData.size):
					self.mazeData.block[x][y].color = MazeBlockColor.green
				self.displayUpdate()
				self.mazeData.block[x] = saved_column		# restore state

				for y in range(self.mazeData.size):
					if ret:
						break
					if self.flag_stopGen:
						return None
					if self.mazeData.block[x][y].color == MazeBlockColor.grey:
						randomDeltaList = MazeDirection.getDeltaList()
						random.shuffle(randomDeltaList)
						for (dir, (dx, dy)) in randomDeltaList:
							nx = x + dx
							ny = y + dy
							if self.isOutOfMaze(nx, ny):
								continue
							if self.mazeData.block[nx][ny].color == MazeBlockColor.white:
								self.mazeData.block[x][y].border[dir] = False
								self.mazeData.block[nx][ny].border[MazeDirection.getOppositeDirDict()[dir]] = False
								ret = (x, y)		# found, assign return value and ready to return
								break

			self.displayUpdate()
			return ret

		huntandkill_iterate_helper(random.randint(0, self.mazeData.size-1),random.randint(0, self.mazeData.size-1))
		while True:
			if self.flag_stopGen:
				return
			try:
				(x, y) = huntandkill_scan_and_add_adjacent()
				huntandkill_iterate_helper(x, y)
			except TypeError:
				break

	def generator_RecursiveDivision(self):		# generator using Recursive Division
		def recursivedivision_helper(x1, y1, x2, y2):
			width = x2 - x1 + 1
			height = y2 - y1 + 1
			if width < 2 or height < 2:
				return
			randomnumber = random.randint(1, width + height)
			if randomnumber <= width:		# vertical wall
				wallx = x1 + random.randint(0, width - 2)
				wally = y1
				passx = wallx
				passy = wally + random.randint(0, height - 1)
				dx = 0
				dy = 1
				wlen = height
				dir = 'r'
			else:		# horizontal wall
				wallx = x1
				wally = y1 + random.randint(0, height - 2)
				passx = wallx + random.randint(0, width - 1)
				passy = wally
				dx = 1
				dy = 0
				wlen = width
				dir = 'd'
			x = wallx
			y = wally
			for i in range(wlen):
				self.mazeData.block[x][y].border[dir] = True
				self.mazeData.block[x+dy][y+dx].border[MazeDirection.getOppositeDirDict()[dir]] = True
				x = x + dx
				y = y + dy
			self.displayUpdate()
			self.mazeData.block[passx][passy].border[dir] = False
			self.mazeData.block[passx+dy][passy+dx].border[MazeDirection.getOppositeDirDict()[dir]] = False
			self.displayUpdate()
			if randomnumber <= width:		# vertical wall
				recursivedivision_helper(x1, y1, wallx, y2)
				recursivedivision_helper(wallx+1, y1, x2, y2)
			else:
				recursivedivision_helper(x1, y1, x2, wally)
				recursivedivision_helper(x1, wally+1, x2, y2)

		recursivedivision_helper(0, 0, self.mazeData.size-1, self.mazeData.size-1)
