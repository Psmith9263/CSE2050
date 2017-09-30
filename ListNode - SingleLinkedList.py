class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def disp(self):
        node = self
        while node:
            print(node.data, '', end='')
            node = node.link

    def disp_rec(self):
        print(self.data, '', end='')
        if self.link:
            self.link.disp_rec()

    def length(self):
        if self.link is None:
            return 1
        return 1 + self.link.length()

    def reverse(self, new_list=None):
        if self.link is None:
            return ListNode(self.data, new_list)
        return self.link.reverse(ListNode(self.data, new_list))

    def reverse2(self):
        lst = self
        new_list = None
        while lst:
            lst.link, lst, new_list = new_list, lst.list, lst
        return new_list
