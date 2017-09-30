from LinkedList import *


class LListStack:
    def __init__(self):
        self._L = LinkedList()

    def push(self, item):
        self._L.addfirst(item)

    def pop(self):
        return self._L.removefirst()

    def __len__(self):
        return self._L.length()
