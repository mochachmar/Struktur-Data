# Moch Achmar_22362_K
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def sort_list(self):
        if self.head is None:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        return sorted_list


linked_list = LinkedList()

input_string = input("Masukkan angka: ")

numbers = [int(digit) for digit in input_string if digit.isdigit()]

for num in numbers:
    linked_list.insert(num)

print("Linked List sebelum diurutkan:")
linked_list.print_list()

linked_list.sort_list()

print("Linked List setelah diurutkan:")
linked_list.print_list()
