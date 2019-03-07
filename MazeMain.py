# -*- coding: utf-8 -*-
import sys

from MazeMainWindowUI import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication


class MazeMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MazeMainWindow, self).__init__()
		self.setupUi(self)
		self.centralwidget.parent().resize(1280, 800)

	def mainFunc_generatorRun(self):
		self.widget_mazeDisplayMain.runNewGenerator(self.comboBox_selectGenerateMethod.currentIndex(),
													self.spinBox_mazeSize.value())

if __name__ == "__main__":
	sys.setrecursionlimit(10000)
	app = QApplication(sys.argv)
	label = MazeMainWindow()
	label.show()
	sys.exit(app.exec_())
