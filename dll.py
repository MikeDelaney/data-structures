class Node(object):
    """
    Represents a node with a pointer to previous node, a value, and a pointer
    to next node.
    """
    def __init__(self, prev=None, val=None, next_node=None):
        self.prev, self.value, self.next_node = prev, val, next_node


class Dll(object):
    """
    Represents a doubly linked list with a head and a tail (initially empty)
    """
    def __init__(self, head=None, tail=None):
        self.tail = self.head = None

    def insert(self, value):
        """
        Inserts a new node at the head of the list.
        """
        if self.head is None:
            self.head = self.tail = Node(val=value)
        else:
            new_node = Node(val=value, next_node=self.head)
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        """
        Adds a new node to the tail of the list
        """
        if self.tail is None:
            self.tail = self.head = Node(val=value)
        else:
            new_node = Node(val=value, prev=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def pop(self):
        """
        Removes the item at the head of the list and returns its value.
        """
        if self.head is None:
            raise LookupError
        retval = self.head.value
        self.head = self.head.next_node
        self.head.prev = None
        return retval

    def shift(self):
        """
        Removes the item at the tail of the list and returns its value.
        """
        if self.tail is None:
            raise LookupError
        retval = self.tail.value
        self.tail = self.tail.prev
        self.tail.next_node = None
        return retval

    def remove(self, val):
        """
        Removes the first item in the list with the given value; otherwise
        raises LookupError
        """
        current = self.head
        while current is not None:
            if current.value == val:
                if current.prev is not None:
                    current.prev.next_node = current.next_node
                else:
                    self.head = current.next_node
                if current.next_node is not None:
                    current.next_node.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next_node
        raise LookupError
