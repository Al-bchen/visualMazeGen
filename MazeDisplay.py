#Visual display of the maze
import threading

from MazeGenerator import MazeGenerator
from MazeData import MazeData

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QPaintEvent
from PyQt5.QtCore import Qt


class MazeDisplay(QWidget):

	def __init__(self, parent):
		super(MazeDisplay, self).__init__(parent)

		size = self.size()

		self.mazeMargin = 10
		self.penSize = 2
		self.mazeData = MazeData()
		self.mazeGenerator = MazeGenerator()
		self.mazeGenerator.setMaze(self.mazeData)
		self.mazeGenerator.setWidget(self)
		self.displaySize = (min(size.height(), size.width()) - 2 * self.mazeMargin) // self.mazeData.size * self.mazeData.size
		self.marginX = (size.width() - self.displaySize) / 2
		self.marginY = (size.height() - self.displaySize) / 2
		self.blockSize = self.displaySize // self.mazeData.size

	def paintEvent(self, e: QPaintEvent):
		qp = QPainter()
		qp.begin(self)

		self.setDisplaySize()
		self.drawMazeBlocks(qp)

		qp.end()

	def setDisplaySize(self):
		size = self.size()
		self.displaySize = (min(size.height(), size.width()) - 2 * self.mazeMargin) // self.mazeData.size * self.mazeData.size
		self.marginX = (size.width() - self.displaySize) / 2
		self.marginY = (size.height() - self.displaySize) / 2
		self.blockSize = self.displaySize // self.mazeData.size

	def drawMazeBorder(self, qp: QPainter):
		qp.setPen(QPen(Qt.black, self.penSize, Qt.SolidLine))
		qp.setBrush(QColor(255, 255, 255))
		qp.drawRect(self.marginX, self.marginY, self.displaySize, self.displaySize)

	def drawMazeBlocks(self, qp: QPainter):
		# draw block color
		qp.setPen(QPen(Qt.black, 0, Qt.NoPen))
		for x in range(self.mazeData.size):
			for y in range(self.mazeData.size):
				qp.setBrush(QColor(self.mazeData.block[x][y].color))
				qp.drawRect(self.marginX + x * self.blockSize, self.marginY + y * self.blockSize, self.blockSize, self.blockSize)
		# draw block text(unimplemented)

		# draw block border/edge
		qp.setPen(QPen(Qt.black, self.penSize, Qt.SolidLine))
		for x in range(self.mazeData.size):
			for y in range(self.mazeData.size):
				if self.mazeData.block[x][y].border['u'] == True:
					qp.drawLine(self.marginX + x * self.blockSize, self.marginY + y * self.blockSize,
								self.marginX + (x + 1) * self.blockSize, self.marginY + y * self.blockSize)
				if self.mazeData.block[x][y].border['d'] == True:
					qp.drawLine(self.marginX + x * self.blockSize, self.marginY + (y + 1) * self.blockSize,
								self.marginX + (x + 1) * self.blockSize, self.marginY + (y + 1) * self.blockSize)
				if self.mazeData.block[x][y].border['l'] == True:
					qp.drawLine(self.marginX + x * self.blockSize, self.marginY + y * self.blockSize,
								self.marginX + x * self.blockSize, self.marginY + (y + 1) * self.blockSize)
				if self.mazeData.block[x][y].border['r'] == True:
					qp.drawLine(self.marginX + (x + 1) * self.blockSize, self.marginY + y * self.blockSize,
								self.marginX + (x + 1) * self.blockSize, self.marginY + (y + 1) * self.blockSize)

	def runNewGenerator(self, index: int, size: int):
		th = threading.Thread(target = self.mazeGenerator.generatorCreateAndRun, args=[index, size], daemon=True)
		th.start()
