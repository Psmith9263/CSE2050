class ListDeque:

    def __init__(self):
        self._L = []

    def addFirst(self, item):
        self._L.insert(0, item)

    def addlast(self, item):
        self._L.append(item)

    def removefirst(self):
        return self._L.pop(0)

    def removelast(self):
        return self._L.pop()