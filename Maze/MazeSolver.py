# Different solver to solve the maze
import random
import time
import threading
import copy

from Maze.MazeBase import *
from MazeDisplay import MazeDisplay


class MazeSolver(object):
    def __init__(self):
        self.mazeData = MazeData()
        self.widget = MazeDisplay(None)

        self.lock_startSolver = threading.Lock()
        self.lock_modify_stopSolver = threading.Lock()

        self.flag_stopSolve = False
        self.flag_skipSolve = False
        self.flag_stepSolve = False

        self.event_stepSolve = threading.Event()

        self.currentIndex = -1

    def setMaze(self, x: MazeData):
        self.mazeData = x 	# shallow copy

    def setWidget(self, x: MazeDisplay):
        self.widget = x

    def action_displayUpdate(self, checkpoint=True):
        if not self.flag_stopSolve and not self.flag_skipSolve:
            time.sleep(0.01)
            self.widget.update()
            if checkpoint:
                self.action_stepCheckpoint()

    def action_stepCheckpoint(self):
        if self.flag_stepSolve:
            self.event_stepSolve.wait()
            self.event_stepSolve.clear()

    def button_reset(self, index: int):
        with self.lock_modify_stopSolver:
            if self.flag_stopSolve:
                return
            self.flag_stopSolve = True
            self.flag_stepSolve = False
            self.event_stepSolve.set()

        with self.lock_startSolver:
            self.flag_stopSolve = False
            self.flag_skipSolve = False
            self.flag_stepSolve = False
            self.event_stepSolve.clear()

            self.currentIndex = index

            self.action_displayUpdate()

    def button_run(self):
        pass

    def button_skip(self):
        pass

    def button_step(self):
        pass
