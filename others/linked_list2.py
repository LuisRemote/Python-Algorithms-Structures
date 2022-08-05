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
    
    def search_list(self, value):

        current_node = self.head
        result_list = []

        if current_node == None:
            return

        while current_node != None:
            if current_node.data == value:
                result_list.append(current_node)
                current_node = current_node.get_next()
            else:
                current_node = current_node.get_next()

        return result_list

    def delete_list(self):

        # start from the beginning
        current_node = self.head

        while current_node:

            # grab the next node
            next_node = current_node.next_node

            # delete the current node
            del current_node.data

            # set the current equal to the next node
            current_node = next_node

    def remove_duplicates(self):

        # grab the first node and the node after the first
        previousNode = self.head
        currentNode = previousNode.next_node

        # build a set to store non-duplicate values
        keys = set([previousNode.data])

        while currentNode != None:
            data = currentNode.data

            # if it is a duplicate
            if data in keys:
                previousNode.next_node = currentNode.next_node
                currentNode = currentNode.next_node

            else:
                keys.add(data)

                # reassign the nodes
                previousNode = currentNode
                currentNode = currentNode.next_node

    def kth_to_last(self, k):

        # if k is negative just return nothing
        if k < 0:
            return None

        # if k is 0 then just print the list
        if k == 0:
            self.traverse()
            return

        # grab the list length
        list_length = self.list_size()

        if k > list_length:
            raise ValueError("You has choosen a K that is longer than the list size.")

        # start from the beginning
        p1 = self.head

        for i in range(1, list_length+1):

            if i >= k:
                print(p1.data)
                p1 = p1.next_node
            else:
                p1 = p1.next_node

    def sum_linked_list(self, linked_list):

        total = 0
        p1 = self.head
        p2 = linked_list.head

        while p1 != None:
            if isinstance(p1.data, (int, float)):
                total = total + p1.data
                p1 = p1.get_next()
            else:
                p1 = p1.get_next()

        while p2 != None:
            if isinstance(p2.data, (int, float)):
                total = total + p2.data
                p2 = p2.get_next()
            else:
                p2 = p2.get_next()

        return print(f"The total is {total}")







###
ll = LinkedList()
ll.insert_front(60)
ll.insert_front(50)
ll.insert_front(40)
ll.insert_front(8)
ll.insert_front(40)
ll.insert_front(50)
ll.insert_end(1)
ll.insert_end(2)
ll.traverse()

print('-'*50)
ll.search_list(50)
print(ll.list_size())
print('-'*50)
print(ll.search_list(2))
print('-'*50)
ll.remove_duplicates()
ll.traverse()
print(ll.list_size())
print('-'*50)
ll.kth_to_last(3)

print('-'*50)
ll.traverse()
ll2 = LinkedList()
ll2.insert_front(1)
ll2.insert_front(3)
ll2.insert_front(4)
ll2.insert_end(10)
print('.')
ll2.traverse()

ll.sum_linked_list(ll2)



















