class Node(object):
    def __init__(self, prev=None, val=None, next_node=None):
        self.prev, self.value, self.next_node = prev, val, next_node


class Dll(object):
    def __init__(self, head=None, tail=None):
        self.tail = self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = self.tail = Node(val=value)
        else:
            new_node = Node(val=value, next_node=self.head)
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        if self.tail is None:
            self.tail = self.head = Node(val=value)
        else:
            new_node = Node(val=value, prev=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            raise LookupError
        retval = self.head.value
        self.head = self.head.next_node
        self.head.prev = None
        return retval

    def shift(self):
        if self.tail is None:
            raise LookupError
        retval = self.tail.value
        self.tail = self.tail.prev
        self.tail.next_node = None
        return retval

    def remove(self, val):
        if self.head is None:
            raise LookupError
        if self.head.value == val:
            self.head = self.head.next_node
            self.head.prev = None
            return
        current = self.head.next_node
        while current.next_node is not None:
            if current.value == val:
                current.prev.next_node = current.next_node
                current.next_node.prev = current.prev
                return
            current = current.next_node
        if self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next_node = None
        else:
            raise LookupError
