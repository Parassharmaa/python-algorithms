from data_structures.LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, value):
        self.linked_list.append(value)

    def dequeue(self):
        removed_head = self.linked_list.delete_head()
        return removed_head

    def is_empty(self):
        return self.linked_list.tail is None

    def peek(self):
        if self.linked_list.head is None:
            return None
        return self.linked_list.head.value

    def __str__(self):
        s = self.linked_list()
        return "<--".join(s)
