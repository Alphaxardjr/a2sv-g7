class Node:
    def __init__(self,value,next:None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begining(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head 
            self.head = node 

    def print_list(self):
        pass

