# Different solver to solve the maze

from Maze.MazeBase import *
from MazeDisplay import MazeDisplay

class MazeSolver(object):
	def __init__(self):
		self.mazeData = MazeData()
		self.widget = MazeDisplay(None)

		self.currentIndex = -1

	def setMaze(self, x: MazeData):
		self.mazeData = x 	# shallow copy

	def setWidget(self, x: MazeDisplay):
		self.widget = x
