class node():
    def __init__(self, val=None, p_next_node=None):
        self.next_node = p_next_node
        self.value = val


class linked_list():
    def __init__(self):
        self.head = node()

    def insert(self, val):
        if self.head.value is not None:
            # new_node = node(self.head.value, self.head.next_node)
            # self.head.next_node = self.head
            new_node = node(val, self.head)
            self.head = new_node
        else:
            self.head.next_node = node()
        self.head.value = val

    def pop(self):
        old_head_value = self.head.value
        if self.head.next_node is not None:
            self.head = self.head.next_node
        else:
            self.head = node()
        return old_head_value

    def size(self):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.next_node
        return count

    def search(self, val):
        n = self.head
        while n.value is not None:
            if n.value == val:
                return n
            n = n.next_node
        return None

    def remove(self, node):
        if self.head == node:
            self.head = self.head.next_node
            return

        n = self.head
        while n.value is not None:
            if n.next_node is node:
                n.next_node = n.next_node.next_node
                return
            n = n.next_node
        raise ValueError

    def __str__(self):
        as_string = "("
        n = self.head
        while n.value is not None:
            if type(n.value) == str:
                as_string = as_string + '\'' + n.value + '\''
            else:
                as_string += str(n.value)
            if n.next_node.value is not None:
                as_string += ", "
            n = n.next_node
        as_string += ")"
        return as_string
