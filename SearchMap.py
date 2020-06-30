import PriorityQueue
import Stack
import Dijkstra
import math

prev = 0
prevs = 0

class SearchMap(Dijkstra.Dijkstra):
    def __init__(self):
        super().__init__()

    def isValidPos(self, x, y):
        if x < 0 or y < 0 or x >= self.mapList[0][0] or y >= self.mapList[0][1]:
            return False
        else:
            return self.mapList[1][y][x] == 1 or self.mapList[1][y][x] == 9 or (10<=self.mapList[1][y][x]<=18) or (20<=self.mapList[1][y][x]<=25)

    def BFS(self):
        que = PriorityQueue.PriorityQueue()
        que.enqueue((self.startPoint[0], self.startPoint[1], -self.dist(self.startPoint[0], self.startPoint[1])))

        while not que.isEmpty():
            here = que.dequeue()
            x, y, _ = here
            if self.mapList[1][y][x] == 9:
                return True
            else:
                self.mapList[1][y][x] = -1
                if self.isValidPos(x, y - 1): que.enqueue((x, y - 1, -self.dist(x, y - 1)));  # 위
                if self.isValidPos(x, y + 1): que.enqueue((x, y + 1, -self.dist(x, y + 1)));  # 아래
                if self.isValidPos(x - 1, y): que.enqueue((x - 1, y, -self.dist(x - 1, y))); # 왼쪽
                if self.isValidPos(x + 1, y): que.enqueue((x + 1, y, -self.dist(x + 1, y))); # 오른쪽
        return False

    def dist(self, x, y, end = None):
        if end == None:
            end = []
            end.append(self.endPoint[0])
            end.append(self.endPoint[1])
        (dx, dy) = (end[0] - x, end[1] - y)
        return math.sqrt(dx*dx + dy*dy)

    def saveMarkPosition(self):
        global prev

        stack = Stack.Stack()
        stack.push((self.startPoint[0], self.startPoint[1], 0))

        while not stack.isEmpty():
            here = stack.pop()
            (x,y,_) = here
            cnt = 0
            self.mapList[1][y][x] = -1
            if self.isValidPos(x, y - 1): stack.push((x, y - 1,1)); prev = 1; cnt += 1 # 위
            if self.isValidPos(x, y + 1): stack.push((x, y + 1,2)); prev = 2; cnt += 1  # 아래
            if self.isValidPos(x - 1, y): stack.push((x - 1, y,3)); prev = 3; cnt += 1 # 왼쪽
            if self.isValidPos(x + 1, y): stack.push((x + 1, y,4)); prev = 4; cnt += 1 # 오른쪽
            if (prev != _) or (cnt > 1):
                prev = _
                if (x,y) not in self.savePoint:
                    self.savePoint.append((x,y))
        if (self.startPoint[0],self.startPoint[1]) in self.savePoint:
            self.savePoint.remove((self.startPoint[0],self.startPoint[1]))

        if (self.endPoint[0], self.endPoint[1]) in self.savePoint:
            self.savePoint.remove((self.endPoint[0],self.endPoint[1]))

        self.savePoint.insert(0,(self.startPoint[0],self.startPoint[1]))
        self.savePoint.append((self.endPoint[0],self.endPoint[1]))

        return False

    def ableMap(self,start = (),end = ()):
        global prevs
        que = PriorityQueue.PriorityQueue()
        que.enqueue((start[0], start[1], -self.dist(start[0], start[1],end),0))
        cnt = 0
        turn = -1
        while not que.isEmpty():

            here = que.dequeue()
            x, y, _ , t = here
            if end[0] == x and end[1] == y:
                que.clear()
                return cnt + turn
            else:
                cnt+=1
                self.mapList[1][y][x] = -1

                if self.isValidPos(x, y - 1): que.enqueue((x, y - 1, -self.dist(x, y - 1,end),1)); prevs = 1;   # 위
                if self.isValidPos(x, y + 1): que.enqueue((x, y + 1, -self.dist(x, y + 1,end),2)); prevs = 2; # 아래
                if self.isValidPos(x - 1, y): que.enqueue((x - 1, y, -self.dist(x - 1, y,end),3)); prevs = 3; # 왼쪽
                if self.isValidPos(x + 1, y): que.enqueue((x + 1, y, -self.dist(x + 1, y,end),4)); prevs = 4; # 오른쪽
                if t != prevs:
                    prevs = t
                    turn += 1
                else:
                    if (x,y) in self.savePoint:
                        turn += 1
        return False


    def convert(self):
        weigth = [[9999 for _ in range(len(self.savePoint))] for _ in range(len(self.savePoint))]
        for i in range(len(self.savePoint) - 1):
            for j in range(i+1,len(self.savePoint)):
                weigth[i][j] = self.ableMap(self.savePoint[i],self.savePoint[j])
                weigth[j][i] = weigth[i][j]

                self.resetMap()

        self.addVertex(len(self.savePoint))
        self.addWeight(weigth)

