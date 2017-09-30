class Queue:
    def __init__(self):
        self._L = []
        self._head = 0

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        if self._head > len(self._L) // 2:
            self._L = self._L[self._head:]
            self._head = 0
        return item

    def isempty(self):
        return len(self._L) == 0
