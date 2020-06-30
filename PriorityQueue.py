
class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def size(self): return len(self.items)
    def clear(self):self.items =[]

    def enqueue(self,item):
        if self.isEmpty():
            self.items.append(item)
        else:
            for i in range(0, len(self.items)):
                if item[2] < self.items[0][2]:
                    self.items.insert(0, item)
                    break
                elif item[2] > self.items[-1][2]:
                    self.items.append(item)
                    break
                elif item[2] <= self.items[i][2]:
                    self.items.insert(i, item)
                    break

    def dequeue(self):
        return self.items.pop(-1)