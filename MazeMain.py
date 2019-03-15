# -*- coding: utf-8 -*-
import sys
import threading

from MazeMainWindowUI import Ui_MainWindow
from Maze.MazeGenerator import MazeGenerator
from Maze.MazeSolver import MazeSolver
from Maze.MazeBase import MazeData

from PyQt5.QtWidgets import QMainWindow, QApplication


class MazeMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MazeMainWindow, self).__init__()
		self.setupUi(self)
		self.centralwidget.parent().resize(800, 600)

		self.mazeData = MazeData(self.spinBox_mazeSize.value())

		self.mazeGenerator = MazeGenerator()
		self.mazeGenerator.setMaze(self.mazeData)
		self.mazeGenerator.setWidget(self.widget_mazeDisplayMain)

		self.mazeSolver = MazeSolver()
		self.mazeSolver.setMaze(self.mazeData)
		self.mazeSolver.setWidget(self.widget_mazeDisplayMain)

		self.widget_mazeDisplayMain.mazeData = self.mazeData
		self.widget_mazeDisplayMain.update()

	def mainFunc_generatorRun(self):
		th = threading.Thread(target=self.mazeGenerator.generatorRun, args=[self.comboBox_generatorMethod.currentIndex(), self.spinBox_mazeSize.value()], daemon=True)
		th.start()

	def mainFunc_generatorStep(self):
		th = threading.Thread(target=self.mazeGenerator.generatorStep, args=[self.comboBox_generatorMethod.currentIndex(), self.spinBox_mazeSize.value()], daemon=True)
		th.start()

	def mainFunc_generatorReset(self):
		th = threading.Thread(target=self.mazeGenerator.generatorReset, args=[self.comboBox_generatorMethod.currentIndex(), self.spinBox_mazeSize.value()], daemon=True)
		th.start()

if __name__ == "__main__":
	sys.setrecursionlimit(10000)
	threading.stack_size(128*1024*1024)
	app = QApplication(sys.argv)
	label = MazeMainWindow()
	label.show()
	sys.exit(app.exec_())
