# from node import Node


class Node:
    def __init__(self, data):
        self.value = data
        # Leave the node initially without a next value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # Set the head and the tail with null values
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Create the new node
        new_node = Node(data)
        # Check whether the linked list has a head node
        if self.head:
            # Point the next node of the new node to the head
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_beginning(self):
        if not self.head:
            print("No Element found in Linkedlist")
            return
        print("Remove Element from Beginning")
        # The "next" node of the head becomes the new head node
        self.head = self.head.next

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_end(self):
        if not self.head:
            print("No Element found in Linkedlist")
            return

        print("Remove Element from End")

        current = self.head

        while current.next != self.tail:
            current = current.next

        self.tail = current
        self.tail.next = None

    def insert_after(self, value, match_value):
        """
        Insert value after a specific value
        """
        if not self.head:
            print("No Element found in Linkedlist")
            return

        new_node = Node(value)
        current = self.head

        while current:
            if current.value == match_value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def remove_after(self, value):
        # It will delete any specific value

        if not self.head:
            print("No Element found in Linkedlist")
            return

        if self.head.value == value:
            self.remove_at_beginning()
            return

        current = self.head
        prev = current

        while current.value != value:
            prev = current
            current = current.next

        temp = current
        current = prev
        current.next = temp.next

    def traverse(self):
        print("Traversing Linkedlist Elements:-")
        if not self.head:
            print("Empty Linked List")
            return

        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def search(self, value):
        if not self.head:
            print("Linked List is Empty")
            return

        current_node = self.head
        while current_node:
            if current_node.value == value:
                print(f"Value Found -> {value}")
                return True
            else:
                current_node = current_node.next


if __name__ == '__main__':
    obj = SinglyLinkedList()
    obj.insert_at_beginning('2')
    obj.insert_at_beginning('1')
    obj.insert_at_beginning('0')

    obj.search('0')

    obj.remove_at_beginning()

    obj.traverse()

    obj.insert_at_end('3')
    obj.insert_at_end('4')
    obj.traverse()

    obj.remove_at_end()
    obj.traverse()

    obj.insert_after('0', '2')
    obj.insert_after('0', '3')
    obj.traverse()

    # delete specific value
    obj.remove_after('0')
    obj.traverse()

    # delete from last
    obj.remove_after('0')
    obj.traverse()

    # delete from first
    obj.remove_after('1')
    obj.traverse()
