class Node():
    def __init__(self, val=None):
        self.value = val
        self.next_node = None


class Queue():
    def __init__(self):
        self.head = None
        self.back = Node()

    def enqueue(self, value):
        self.back.next_node = Node(value)
        self.back = self.back.next_node
        if self.head is None:
            self.head = self.back

    def dequeue(self):
        if self.head is None:
            raise LookupError
        retval = self.head.value
        self.head = self.head.next_node
        return retval

    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next_node
        return size
