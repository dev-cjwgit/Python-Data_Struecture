import Player
import random
import Infix2Postfix


class Game(Player.Player):
    def __init__(self):
        super().__init__()
        self.Infix = Infix2Postfix.Infix()

    def calcN(self):
        self.Infix.add(self.inventory)
        postfix1 = self.Infix.Infix2Postfix()
        return self.Infix.evalPostfix(postfix1)

    def printWorld(self):
        print('\n'*100)
        super().printMap()
        self.printInventory()

    def spawnItem(self):
        for i in range(10,19): # 맵에 숫자를 생성함
            tmpX = 0
            tmpY = 0
            while(self.mapList[1][tmpY][tmpX] != 1 or self.arritems(tmpX,tmpY)): #+- 1 범위내 아이텝이 없으면 탈출
                tmpX = random.randint(0, self.X - 1) #아이템이 있으면 X,Y를 다시 설정
                tmpY = random.randint(0, self.Y - 1)
            self.mapList[1][tmpY][tmpX] = i

        # 맵에 더하기를 생성함
        tmpX = 0
        tmpY = 0
        while (self.mapList[1][tmpY][tmpX] != 1 or self.arritems(tmpX,tmpY)):
            tmpX = random.randint(0, self.X - 1)
            tmpY = random.randint(0, self.Y - 1)
        self.mapList[1][tmpY][tmpX] = 22

        for i in range(5): # 맵에 연산자를 생성함
            tmpX = 0
            tmpY = 0
            while (self.mapList[1][tmpY][tmpX] != 1 or self.arritems(tmpX,tmpY)):
                tmpX = random.randint(0, self.X - 1)
                tmpY = random.randint(0, self.Y - 1)
            self.mapList[1][tmpY][tmpX] = i + 20
