import PriorityQueue

INF = 999
class Dijkstra(PriorityQueue.PriorityQueue):
    def __init__(self):
        self.vertex = []
        self.weight = []
        self.vertexList = []

        for i in range(9424, 9450):
            self.vertexList.append(chr(i))

        for i in range(9372, 9398):
            self.vertexList.append(chr(i))

        for i in range(9312, 9327):
            self.vertexList.append(chr(i))

        for i in range(9332, 9347):
            self.vertexList.append(chr(i))


    def addVertex(self,cnt):
        for i in range(cnt):
            self.vertex.append(self.vertexList[i])

    def addWeight(self,lst):
        self.weight = lst

    def choose_vertex(self,dist, found):
        min = INF
        minpos = -1
        for i in range(len(dist)):
            if dist[i] < min and found[i] == False:
                min = dist[i]
                minpos = i
        return minpos

    def shortest_path_dijkstra(self, start):
        vsize = len(self.vertex)
        dist = list(self.weight[start])
        path = [start] * vsize
        found = [False] * vsize
        found[start] = True
        dist[start] = 0
        for i in range(vsize):
            # print("Step%2d: "%(i+1),dist)
            u = self.choose_vertex(dist, found)
            found[u] = True
            for w in range(vsize):
                if not found[w]:
                    if dist[u] + self.weight[u][w] < dist[w]:
                        dist[w] = dist[u] + self.weight[u][w]
                        path[w] = u
        return path

    def printPath(self,start = 0):
        path = self.shortest_path_dijkstra(0)
        end = len(self.vertex) - 1
        if end != start:
            print('경로 [%s->%s] %s'%(self.vertex[start],self.vertex[end],self.vertex[end]),end = '')
            while path[end] != start:
                print(" <- %s" % self.vertex[path[end]],end = '')
                end = path[end]
            print(' <- %s'%self.vertex[path[end]])
