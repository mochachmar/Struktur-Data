# Moch Achmar_22362_K
import sys


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def children_count(self):
        if self.left is None and self.right is None:
            return None

        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        if data == self.data:
            return self, parent
        elif data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        else:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.data = n.data
                    self.left = n.left
                    self.right = n.right
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                del node

    def preorder(self):
        def preorder_traversal(node):
            if node is not None:
                sys.stdout.write(str(node.data) + " -> ")
                preorder_traversal(node.left)
                preorder_traversal(node.right)
        preorder_traversal(self)
        print("None")

    def inorder(self):
        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                sys.stdout.write(str(node.data) + " -> ")
                inorder_traversal(node.right)
        inorder_traversal(self)
        print("None")

    def postorder(self):
        def postorder_traversal(node):
            if node is not None:
                postorder_traversal(node.left)
                postorder_traversal(node.right)
                sys.stdout.write(str(node.data) + " -> ")
        postorder_traversal(self)
        print("None")


def main():
    # KADABRA
    kadabra = Node('K')
    kadabra.insert('A')
    kadabra.insert('D')
    kadabra.insert('A')
    kadabra.insert('B')
    kadabra.insert('R')
    kadabra.insert('A')

    print('Inorder Traversal for KADABRA:')
    kadabra.inorder()
    print()

    print('Preorder Traversal for KADABRA:')
    kadabra.preorder()
    print()

    print('Postorder Traversal for KADABRA:')
    kadabra.postorder()
    print()

    # MINAKJINGGO
    minakjinggo = Node('M')
    minakjinggo.insert('I')
    minakjinggo.insert('N')
    minakjinggo.insert('A')
    minakjinggo.insert('K')
    minakjinggo.insert('J')
    minakjinggo.insert('I')
    minakjinggo.insert('N')
    minakjinggo.insert('G')
    minakjinggo.insert('G')
    minakjinggo.insert('O')

    print('Inorder Traversal for MINAKJINGGO:')
    minakjinggo.inorder()
    print()

    print('Preorder Traversal for MINAKJINGGO:')
    minakjinggo.preorder()
    print()

    print('Postorder Traversal for MINAKJINGGO:')
    minakjinggo.postorder()
    print()


if __name__ == '__main__':
    main()
