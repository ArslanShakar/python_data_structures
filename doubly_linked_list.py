# Online Python - IDE, Editor, Compiler, Interpreter

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.data = data

        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

    def traverse(self):
        if not self.head:
            print('list is empty')
            return
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def delete_from_start(self):
        print('Delete one element from start.')
        if not self.head:
            print('list is empty')
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_from_end(self):
        print('Delete one element from End.')

        if not self.head:
            print('list is empty')
            return
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.prev.next = None
        curr.prev = None

    def reverse_traversing(self):
        print('Reverse Traverse')
        if not self.head:
            print('list is empty')
            return
        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data)
            temp = temp.prev


obj = DoublyLinkedlist()

print('Inserting at Start:')
obj.insert_at_first(1)
obj.insert_at_first(2)
obj.insert_at_first(3)
obj.traverse()

obj.reverse_traversing()

print('Inserting at End:')
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.traverse()

obj.delete_from_start()
obj.traverse()
obj.delete_from_start()
obj.traverse()

obj.delete_from_end()
obj.traverse()
obj.delete_from_end()
obj.traverse()
