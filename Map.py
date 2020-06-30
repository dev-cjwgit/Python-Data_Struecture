import SearchMap

class Map(SearchMap.SearchMap):
    def __init__(self):
        super().__init__()
        self.mapList = None
        self.startPoint = []
        self.endPoint = []
        self.savePoint = []
        self.blankCnt = 0

    def readMap(self, str):
        self.blankCnt = 0
        try:
            fp = open(str, 'r')
            buffer = fp.read()
            self.X = int(buffer.split('\n')[0].split(' ')[0])  # Map의 X정보
            self.Y = int(buffer.split('\n')[0].split(' ')[1])  # Map의 Y정보
            self.mapList = [[self.X, self.Y], []]
            for i, value in enumerate(buffer.split('\n')[1]):
                if (i % int(self.mapList[0][0]) == 0):
                    self.mapList[1].append([])
                self.mapList[1][(i) // int(self.mapList[0][0])].append(int(value))
                if int(value) == 5:
                    self.startPoint.append(i % int(self.mapList[0][0]))
                    self.startPoint.append(i // int(self.mapList[0][0]))
                elif int(value) == 9:
                    self.endPoint.append(i % int(self.mapList[0][0]))
                    self.endPoint.append(i // int(self.mapList[0][0]))
                elif int(value) == 0:
                    self.blankCnt+=1

            fp.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def resetMap(self):
        for i, value in enumerate(self.mapList[1]):
            for _, j in enumerate(value):
                if not (j == 0 or j == 5 or j == 9):
                    self.mapList[1][i][_] = 1

        self.mapList[1][self.startPoint[1]][self.startPoint[0]] = 5
        self.mapList[1][self.endPoint[1]][self.endPoint[0]] = 9

    def printMap(self):
        for i, value in enumerate(self.mapList[1]):
            for _, j in enumerate(value):
                char = None
                if j == 0:
                    char = '■'
                elif j == 1:
                    char = '　'
                elif j == 5:
                    char = 'ⓢ'
                elif j == 9:
                    char = 'ⓔ'
                elif j == -1:
                    char = '□'
                elif j == 10:
                    char = '①'
                elif j == 11:
                    char = '②'
                elif j == 12:
                    char = '③'
                elif j == 13:
                    char = '④'
                elif j == 14:
                    char = '⑤'
                elif j == 15:
                    char = '⑥'
                elif j == 16:
                    char = '⑦'
                elif j == 17:
                    char = '⑧'
                elif j == 18:
                    char = '⑨'
                elif j == 20:
                    char = '（'
                elif j == 21:
                    char = '）'
                elif j == 22:
                    char = '＋'
                elif j == 23:
                    char = '―'
                elif j == 24:
                    char = 'Ｘ'
                else:
                    char = j
                #elif j == 25:
                #    char = '÷'

                print('%s'%char, end='')
            print()

    def writeVertex(self):
        for i,val in enumerate(self.savePoint):
            self.mapList[1][val[1]][val[0]] = self.vertex[i]