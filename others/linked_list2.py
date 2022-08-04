# Linked List in Python
# YouTube: Sigma Coding

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Returns the data"""
        return self.data

    def get_next(self):
        """ Returns the next node """
        return self.next_node

    def set_next(self, new_next):
        """ Declare next_node as new_node """
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def insert_front(self, data):

        # define a new node
        new_node = Node(data)

        # set the 2nd node to equal the old first one
        new_node.set_next(self.head)

        # the new head will be the new node
        self.head = new_node

    def insert_end(self, data):

        # define a new node
        new_node = Node(data)
        head_node = self.head

        if head_node is None:
            head_node = new_node
            return

        # otherwise, let's find the Last node
        last_node = head_node

        # as long as there is a next node it means we haven't reached the end
        while last_node.get_next() != None:
            last_node = last_node.get_next()

        # when we reach the end, set the node
        last_node.set_next(new_node)
        self.end = new_node

    def insert_middle(self, middle_node, data):

        if middle_node is None:
            print("The node you've selected doesn't exist.")

        new_node = Node(data)
        new_node.set_next(middle_node.get_next())
        middle_node.set_next(new_node)

    def traverse(self):

        # define the first node
        node = self.head

        while node != None: # NOTE the while sintaxis
            print(node.get_data())
            node = node.get_next()


    def list_size(self):

        current_node = self.head
        current_count = 0

        while current_node: # NOTE the while sintaxis
            current_count += 1
            current_node = current_node.get_next()

        return current_count

    def delete_node(self, value):

        current_node = self.head
        found = False
        previous_node = None

        if current_node == None:
            return

        while current_node != None and found is False:
            if current_node.data == value:
                found = True
                break
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data not in list")

        if previous_node is None:
            # then it was the head node, the new head is the node after the first
            self.head = current_node.get_next()
        else:
            # otherwise take the previous node and set the node after it to be the one
            # that contains value and comes after it
            previous_node.set_next(current_node.get_next())






















