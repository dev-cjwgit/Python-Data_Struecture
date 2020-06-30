import Map


class Player(Map.Map):
    def __init__(self):
        super().__init__()
        self.inventory = []
        self.temp = None
        self.status = 0

    def printInventory(self):
        print('Items : ',self.inventory)

    def dropItem(self):
        if self.arritems(self.startPoint[0],self.startPoint[1]) or self.temp is not None:
            print('주변에 아이템이 있으므로 버리는것이 불가능합니다')
        else:
            if len(self.inventory) > 0:
                self.status = 1
                self.temp = self.inventory[-1]

                if self.temp == '（':
                    self.temp = 20
                elif self.temp == '）':
                    self.temp = 21
                elif self.temp == '＋':
                    self.temp = 22
                elif self.temp == '―':
                    self.temp = 23
                elif self.temp == 'Ｘ':
                    self.temp = 24
                elif 1 <= self.temp <= 9:
                    self.temp+=9
                self.inventory.pop(-1)

            else:
                print('버릴 아이템이 없습니다.')

    def getItem(self):
        if self.temp != 0 and self.temp is not None:
            if 10 <= self.temp <= 18:
                self.inventory.append(self.temp - 9)
            elif 20 <= self.temp <= 25:
                char = ''
                if self.temp == 20:
                    char = '（'
                elif self.temp == 21:
                    char = '）'
                elif self.temp == 22:
                    char = '＋'
                elif self.temp == 23:
                    char = '―'
                elif self.temp == 24:
                    char = 'Ｘ'
                elif self.temp == 25:
                    char = '÷'

                self.inventory.append(char)

            self.status = 0
            self.temp = None
            self.mapList[1][self.startPoint[1]][self.startPoint[0]] = 1

            self.printInventory()
        else:
            print('아이템이 없습니다.')

    def arritems(self,x,y): #범위 내 아이템 및 시작, 끝점이 있으면 True
        return (10<=self.mapList[1][y+1][x]<=24) or (10<=self.mapList[1][y-1][x]<=24) or (10<=self.mapList[1][y][x+1]<=24) or (10<=self.mapList[1][y][x-1]<=24) or self.mapList[1][y+1][x] == 5 or self.mapList[1][y-1][x] == 5 or self.mapList[1][y][x+1] == 5 or self.mapList[1][y][x-1] == 5    or self.mapList[1][y+1][x] == 9 or self.mapList[1][y-1][x] == 9 or self.mapList[1][y][x+1] == 9 or self.mapList[1][y][x-1] == 9

    def movePlayer(self,x,y):
        self.status = 0
        if self.isValidPos(self.startPoint[0] + x, self.startPoint[1] + y) == True:
            if self.mapList[1][self.startPoint[1] + y][self.startPoint[0] + x] == 9:
                return True
            elif (10 <= self.mapList[1][self.startPoint[1] + y][self.startPoint[0] + x] <= 18) or (20 <= self.mapList[1][self.startPoint[1] + y][self.startPoint[0] + x] <= 25):
                self.temp = self.mapList[1][self.startPoint[1] + y][self.startPoint[0] + x]
                self.status = 1

            if self.temp is not None and self.status == 0:
                self.mapList[1][self.startPoint[1]][self.startPoint[0]] = self.temp
                self.temp=None
            else:
                self.mapList[1][self.startPoint[1]][self.startPoint[0]] = 1

            self.mapList[1][self.startPoint[1] + y][self.startPoint[0] + x] = 5
            self.startPoint[1]+=y
            self.startPoint[0]+=x

            self.printWorld()