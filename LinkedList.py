from ListNode import *


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None: self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None: self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link

            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return item

    def __len__(self):
        return self._length

    def display(self):
        node = self._head
        while node:
            print(node.data, end=' ')
            node = node.link
        print()

    def alldata(self):
        L = []
        cur = self._head
        while cur is not None:
            L.append(cur.data)
            cur = cur.link
        return L

    def length(self):
        node = self._head
        count = 0
        while node:
            node = node.link
            count += 1
        return count
