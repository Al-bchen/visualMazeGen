class MazeBlockColor(object):
    white = '#ffffff'
    black = '#000000'
    grey = '#c0c0c0'
    cyan = '#00ffff'
    dark_cyan = '#008080'
    green = '#77ff77'


class MazeBlockData(object):
    def __init__(self):
        # Border / Edge
        self.border = dict()
        self.border['u'] = self.border['d'] = self.border['l'] = self.border['r'] = False

        # Color
        self.color = MazeBlockColor.white

        # Text
        self.text = ''


class MazeDirection(object):
    @staticmethod
    def getDeltaList():
        return [('u', (0, -1)), ('d', (0, 1)), ('l', (-1, 0)), ('r', (1, 0))]

    @staticmethod
    def getDeltaDict():
        return dict(MazeDirection.getDeltaList())

    @staticmethod
    def getOppositeDirDict():
        return {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}

    @staticmethod
    def getDeltaList_twoDir():
        return [('d', (0, 1)), ('r', (1, 0))]

    @staticmethod
    def getDeltaDict_twoDir():
        return dict(MazeDirection.getDeltaList_twoDir())


class MazeData(object):
    def __init__(self, x=5):
        self.size = x
        self.isGenerated = False
        self.isReset = False
        self.isSolving = False
        self.block = []
        self.initMaze()

    def setSize(self, x: int):
        self.size = x
        self.initMaze()

    def initMaze(self):
        self.initMaze_grey()

    def initMaze_grey(self):
        self.block = [[MazeBlockData() for _i in range(self.size)] for _j in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                self.block[x][y].color = MazeBlockColor.grey
                self.block[x][y].border['u'] \
                    = self.block[x][y].border['d'] \
                    = self.block[x][y].border['l'] \
                    = self.block[x][y].border['r'] = True
        self.isGenerated = False
        self.isReset = True
        self.isSolving = False

    def initMaze_white(self):
        self.block = [[MazeBlockData() for _i in range(self.size)] for _j in range(self.size)]
        for i in range(self.size):
            self.block[i][0].border['u'] = True
            self.block[i][self.size - 1].border['d'] = True
            self.block[0][i].border['l'] = True
            self.block[self.size - 1][i].border['r'] = True
        self.isGenerated = False
        self.isReset = True
        self.isSolving = False
