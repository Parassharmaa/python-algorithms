from data_structures.linked_list.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        return self.linked_list.tail is None

    def peek(self):
        if (self.is_empty()):
            return None
        return self.linked_list.tail.value

    def push(self, value):
        self.linked_list.append(value)

    def pop(self):
        removedTail = self.linked_list.delete_tail()
        return removedTail.value if removedTail else None

    def __call__(self):
        l = self.linked_list()
        return l[::-1]

    def __str__(self):
        return str(self.linked_list)
