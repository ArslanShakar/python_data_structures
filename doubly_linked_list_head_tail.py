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
            self.tail = new_node
            print(f"First element inserted = {data}")
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            print(f"{data} inserted at first")

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            print(f"First element inserted = {data}")
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(f"{data} inserted at end")

    def traverse(self):
        if not self.head:
            print('list is empty')
            return

        print("Forward Traversing")
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
        self.tail = self.tail.prev
        self.tail.next = None

    def reverse_traversing(self):
        if not self.head:
            print('list is empty')
            return
        print("Reverse Traversing")
        temp = self.tail

        while temp.prev:
            print(temp.data)
            temp = temp.prev

        print(temp.data)


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

obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.reverse_traversing()
