class List:
    def __init__(self, _nextNode=None):
        self.val = 0
        self.next = _nextNode

    def getNextNode(self):
        return self.next

    def setNextNode(self, _nextNode=None):
        self.next = _nextNode

    def getval(self):
        return self.val

    def setVal(self, _val):
        self.val = _val

class CyclesQueueList:
    def __init__(self, size):
        self._size = size
        self._count = 0
        temp = List()
        first = temp
        for i in range(size - 1):
            temp = List(temp)
        first.setNextNode(temp)
        self._head = first
        self._tail = first

    def size(self):
        return self._size

    def count(self):
        return self._count

    def empty(self):
        return self._count == 0

    def full(self):
        return self._count == self._size

    def push(self, el):
        if self.full():
            raise Exception("Очередь полная")

        self._head.setVal(el)
        self._count += 1
        self._head = self._head.getNextNode()

    def pop(self):
        if self.empty():
            raise Exception("Очередь пустая")

        item = self._tail.getval()

        self._count -= 1

        self._tail = self._tail.getNextNode()
        return item