
class Node:
    """Class representing a node in a singly linked list."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other
    

class SingleList:
    """Class representing a singly linked list."""

    def __init__(self):
        self.length = 0   
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):   
        return self.length

    def insert_head(self, node):
        if self.head:   
            node.next = self.head
            self.head = node
        else:   
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   
        if self.head:  
            self.tail.next = node
            self.tail = node
        else:   
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  
        if self.is_empty():
            raise ValueError('List is empty')
        node = self.head
        if self.head == self.tail:   
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   
        self.length -= 1
        return node   
    
    #------------added methods------------------
    def search(self, data):
        curr_node = self.head
        while curr_node and curr_node.data != data:
            curr_node = curr_node.next
        return curr_node
    
    def find_min(self):
        if self.head is None:
            return None
        min_val_node = self.head
        curr_node = self.head.next
        while curr_node:
            if min_val_node.data > curr_node.data:
                min_val_node = curr_node
            curr_node = curr_node.next
        return min_val_node

    def find_max(self):
        if self.head is None:
            return None
        max_val_node = self.head
        curr_node = self.head.next
        while curr_node:
            if max_val_node.data < curr_node.data:
                max_val_node = curr_node
            curr_node = curr_node.next
        return max_val_node

    def reverse(self):
        prev_node = None
        curr_node = self.head
        self.tail = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node



 