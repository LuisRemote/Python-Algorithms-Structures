# Python Data Structures #2: Linked List
# YouTube: Brian Faure

class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        elements = 0
        while current.next != None:
            elements += 1
            current = current.next
        return elements

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements

    def get(self, index):
        if index >= self.length():
            print ("Error: 'Get' Index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        current_index = 0
        current_node=self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_list = Linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


print(my_list.display())
print("Element at 2do index: {}".format(my_list.get(2)))

my_list.erase(2)
print(my_list.display())




