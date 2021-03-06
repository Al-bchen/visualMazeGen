# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MazeMainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_generatorMethod = QtWidgets.QWidget(self.centralwidget)
        self.widget_generatorMethod.setObjectName("widget_generatorMethod")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_generatorMethod)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_generatorMethod = QtWidgets.QComboBox(self.widget_generatorMethod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_generatorMethod.sizePolicy().hasHeightForWidth())
        self.comboBox_generatorMethod.setSizePolicy(sizePolicy)
        self.comboBox_generatorMethod.setObjectName("comboBox_generatorMethod")
        self.comboBox_generatorMethod.addItem("")
        self.comboBox_generatorMethod.addItem("")
        self.comboBox_generatorMethod.addItem("")
        self.comboBox_generatorMethod.addItem("")
        self.comboBox_generatorMethod.addItem("")
        self.comboBox_generatorMethod.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_generatorMethod)
        self.widget_generatorConfig = QtWidgets.QWidget(self.widget_generatorMethod)
        self.widget_generatorConfig.setObjectName("widget_generatorConfig")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_generatorConfig)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_generatorSize = QtWidgets.QWidget(self.widget_generatorConfig)
        self.widget_generatorSize.setObjectName("widget_generatorSize")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_generatorSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_mazeSize = QtWidgets.QLabel(self.widget_generatorSize)
        self.label_mazeSize.setObjectName("label_mazeSize")
        self.horizontalLayout_3.addWidget(self.label_mazeSize)
        self.spinBox_mazeSize = QtWidgets.QSpinBox(self.widget_generatorSize)
        self.spinBox_mazeSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_mazeSize.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_mazeSize.setMinimum(5)
        self.spinBox_mazeSize.setMaximum(50)
        self.spinBox_mazeSize.setProperty("value", 20)
        self.spinBox_mazeSize.setObjectName("spinBox_mazeSize")
        self.horizontalLayout_3.addWidget(self.spinBox_mazeSize)
        self.pushButton_generatorRun = QtWidgets.QPushButton(self.widget_generatorSize)
        self.pushButton_generatorRun.setObjectName("pushButton_generatorRun")
        self.horizontalLayout_3.addWidget(self.pushButton_generatorRun)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.widget_generatorSize)
        self.widget_generatorPushButton = QtWidgets.QWidget(self.widget_generatorConfig)
        self.widget_generatorPushButton.setObjectName("widget_generatorPushButton")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_generatorPushButton)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_generatorReset = QtWidgets.QPushButton(self.widget_generatorPushButton)
        self.pushButton_generatorReset.setObjectName("pushButton_generatorReset")
        self.horizontalLayout_4.addWidget(self.pushButton_generatorReset)
        self.pushButton_generatorStep = QtWidgets.QPushButton(self.widget_generatorPushButton)
        self.pushButton_generatorStep.setEnabled(True)
        self.pushButton_generatorStep.setObjectName("pushButton_generatorStep")
        self.horizontalLayout_4.addWidget(self.pushButton_generatorStep)
        self.pushButton_generatorSkip = QtWidgets.QPushButton(self.widget_generatorPushButton)
        self.pushButton_generatorSkip.setEnabled(True)
        self.pushButton_generatorSkip.setObjectName("pushButton_generatorSkip")
        self.horizontalLayout_4.addWidget(self.pushButton_generatorSkip)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.widget_generatorPushButton)
        self.horizontalLayout.addWidget(self.widget_generatorConfig)
        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_generatorMethod)
        self.widget_mazeDisplay = QtWidgets.QWidget(self.centralwidget)
        self.widget_mazeDisplay.setMinimumSize(QtCore.QSize(400, 400))
        self.widget_mazeDisplay.setObjectName("widget_mazeDisplay")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_mazeDisplay)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_mazeDisplayMain = MazeDisplay(self.widget_mazeDisplay)
        self.widget_mazeDisplayMain.setObjectName("widget_mazeDisplayMain")
        self.horizontalLayout_2.addWidget(self.widget_mazeDisplayMain)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addWidget(self.widget_mazeDisplay)
        self.widget_selectSolveMethod = QtWidgets.QHBoxLayout()
        self.widget_selectSolveMethod.setObjectName("widget_selectSolveMethod")
        self.comboBox_solverMethod = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_solverMethod.setEnabled(False)
        self.comboBox_solverMethod.setObjectName("comboBox_solverMethod")
        self.comboBox_solverMethod.addItem("")
        self.comboBox_solverMethod.addItem("")
        self.comboBox_solverMethod.addItem("")
        self.comboBox_solverMethod.addItem("")
        self.widget_selectSolveMethod.addWidget(self.comboBox_solverMethod)
        self.pushButton_solverReset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solverReset.setEnabled(False)
        self.pushButton_solverReset.setObjectName("pushButton_solverReset")
        self.widget_selectSolveMethod.addWidget(self.pushButton_solverReset)
        self.pushButton_solverStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solverStep.setEnabled(False)
        self.pushButton_solverStep.setObjectName("pushButton_solverStep")
        self.widget_selectSolveMethod.addWidget(self.pushButton_solverStep)
        self.pushButton_solverRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solverRun.setEnabled(False)
        self.pushButton_solverRun.setObjectName("pushButton_solverRun")
        self.widget_selectSolveMethod.addWidget(self.pushButton_solverRun)
        self.pushButton_solverRun_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solverRun_4.setEnabled(False)
        self.pushButton_solverRun_4.setObjectName("pushButton_solverRun_4")
        self.widget_selectSolveMethod.addWidget(self.pushButton_solverRun_4)
        self.widget_selectSolveMethod.setStretch(0, 100)
        self.widget_selectSolveMethod.setStretch(3, 1)
        self.verticalLayout.addLayout(self.widget_selectSolveMethod)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_generatorRun.clicked.connect(MainWindow.mainFunc_generatorRun)
        self.pushButton_generatorStep.clicked.connect(MainWindow.mainFunc_generatorStep)
        self.pushButton_generatorReset.clicked.connect(MainWindow.mainFunc_generatorReset)
        self.pushButton_generatorSkip.clicked.connect(MainWindow.mainFunc_generatorSkip)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maze - bchen111"))
        self.comboBox_generatorMethod.setItemText(0, _translate("MainWindow", "Recursive Backtracking / Depth First Search"))
        self.comboBox_generatorMethod.setItemText(1, _translate("MainWindow", "Kruskal\'s Algorithm"))
        self.comboBox_generatorMethod.setItemText(2, _translate("MainWindow", "Prim\'s Algorithm"))
        self.comboBox_generatorMethod.setItemText(3, _translate("MainWindow", "Hunt And Kill"))
        self.comboBox_generatorMethod.setItemText(4, _translate("MainWindow", "Recursive Division"))
        self.comboBox_generatorMethod.setItemText(5, _translate("MainWindow", "Eller\'s Algorithm"))
        self.label_mazeSize.setText(_translate("MainWindow", "Maze size (5-50)"))
        self.pushButton_generatorRun.setText(_translate("MainWindow", "Run"))
        self.pushButton_generatorReset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_generatorStep.setText(_translate("MainWindow", "Step"))
        self.pushButton_generatorSkip.setText(_translate("MainWindow", "Skip"))
        self.comboBox_solverMethod.setItemText(0, _translate("MainWindow", "Depth First Search"))
        self.comboBox_solverMethod.setItemText(1, _translate("MainWindow", "Breadth First Search"))
        self.comboBox_solverMethod.setItemText(2, _translate("MainWindow", "Dijkstra Algorithm"))
        self.comboBox_solverMethod.setItemText(3, _translate("MainWindow", "A* Algorithm"))
        self.pushButton_solverReset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_solverStep.setText(_translate("MainWindow", "Step"))
        self.pushButton_solverRun.setText(_translate("MainWindow", "Run"))
        self.pushButton_solverRun_4.setText(_translate("MainWindow", "Skip"))


from MazeDisplay import MazeDisplay
