# Moch Achmar_22362_K
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.back = self.tail
            self.tail = new_node

    def add_after(self, node, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == node:
                new_node.next = current.next
                new_node.back = current
                current.next = new_node
            current = current.next
        if new_node.next is not None:
            new_node.next.back = new_node

    def add_before(self, node, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == node:
                new_node.back = current.back
                new_node.next = current
                current.back = new_node
            current = current.next
        if new_node.back is not None:
            new_node.back.next = new_node

    def remove(self, node):
        current = self.head
        if self.head.data == node:
            self.head = node.next
        if self.tail.data == node:
            self.tail = node.back
        else:
            while current:
                if current.data == node:
                    current.next.back = current.back
                    current.back.next = current.next
                current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <=> ")
            current = current.next
        print("None")

    def print_Back(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <=> ")
            current = current.back
        print("None")


def main():
    dll = DoublyLinkedList()
    dll.add_first(1)
    dll.add_last(2)
    dll.add_last(3)
    dll.add_last(4)

    dll.print_list()
    dll.print_Back()


main()
