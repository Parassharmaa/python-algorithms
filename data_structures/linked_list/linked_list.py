class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        self.head = Node(value, self.head)
        return self

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            return self
        self.tail.next = new_node
        self.tail = new_node
        return self

    def delete(self, value):
        if self.head is None:
            return None

        deleted_node = None
        while self.head and self.head.value == value:
            deleted_node = self.head
            self.head = self.head.next

        current_node = self.head

        if current_node is not None:
            while current_node.next:
                if current_node.next.value == value:
                    deleted_node = current_node.next
                    current_node.next = deleted_node.next
                else:
                    current_node = current_node.next

            if self.tail == value:
                self.tail = current_node

            return deleted_node

    def find(self, value):
        if self.head is None:
            return self

        current_node = self.head

        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        return None

    def delete_tail(self):
        if self.head == self.tail:
            deleted_tail = self.tail
            self.head = None
            self.tail = None

            return deleted_tail

        deleted_tail = self.tail

        current_node = self.head

        while current_node.next:
            if current_node.next.next is None:
                current_node.next = None
            else:
                current_node = current_node.next

        self.tail = current_node
        return deleted_tail

    def delete_head(self):
        if self.head is None:
            return None

        delete_head = self.head

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        return delete_head

    def __call__(self):
        nodes = []

        current_node = self.head

        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.next

        return nodes

    def __str__(self):
        s = list(map(str, self.__call__()))
        return "-->".join(s)
