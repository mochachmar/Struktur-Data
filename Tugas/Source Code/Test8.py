# Moch Achmar_22362_K
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("Circular Linked List is empty.")
        else:
            while True:
                print(current_node.data)
                current_node = current_node.next
                if current_node == self.head:
                    break

    def insert_node_in_middle(self, list, thisdata, data):
        # insert data after thisdata
        if list.head is None:
            list.head = Node(data)
            list.tail = list.head
        else:
            current_node = list.head
            while current_node.data != thisdata:
                current_node = current_node.next
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def delete_node(self, list, data):
        if list.head is None:
            return
        current_node = list.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    list.head = current_node.next
                else:
                    previous_node.next = current_node.next
                if current_node == list.tail:
                    list.tail = previous_node
                break
            previous_node = current_node
            current_node = current_node.next

    def insert_node_sorted(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        elif data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        elif data >= self.tail.data:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            current_node = self.head
            while current_node.next.data < data:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node


if __name__ == "__main__":
    my_list = CircularLinkedList()
    print("add 3 nodes")
    my_list.add_node(1)
    my_list.add_node(2)
    my_list.add_node(3)
    print("Insert a node in the middle")
    my_list.insert_node_in_middle(my_list, 2, 4)
    my_list.print_list()
    print("Insert a node in sorted order")
    my_list.insert_node_sorted(0)
    my_list.insert_node_sorted(5)
    my_list.print_list()
    print("delete node 2")
    my_list.delete_node(my_list, 2)
    my_list.print_list()
