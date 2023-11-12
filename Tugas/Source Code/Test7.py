# Moch Achmar_22362_K
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Untaian:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def delete_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_at_head(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


queue = Untaian()
for i in range(1, 11):
    queue.delete_at_tail(i)

print("Isi antrian sebelum pelayanan:")
queue.traverse()

for _ in range(3):
    served_data = queue.delete_at_head()
    print("Melayani data:", served_data)

print("Isi antrian setelah pelayanan:")
queue.traverse()
