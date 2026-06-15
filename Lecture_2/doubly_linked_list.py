#Here we are gonna implement a doubly linked list in python

class node(object):
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_first(self, val):
        if self.head != None:
            new_node = node(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            new_node = node(val)
            self.head = new_node
            self.tail = new_node

    def insert_last(self, val):
        if self.tail != None:
            new_node = node(val)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:
            new_node = node(val)
            self.tail = new_node
            self.head = new_node

    def insert_after(self, val, node_bef):
        new_node = node(val)

        current = self.head

        while current.value != node_bef:
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node


    def insert_before(self, val, node_aft):
        new_node = node(val)

        current = self.head

        while current.value != node_aft:
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        new_node.prev.next = new_node

    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        self.last = self.last.prev
        self.last.next = None

    def display(self):
        current = self.head

        print(None, end = "<->")

        while current:
            print(current.value, end = "<->")
            current = current.next
        print(None)


l1 = doubly_linked_list()

l1.insert_last(1)
l1.insert_last(2)
l1.insert_last(3)
l1.insert_last(4)
l1.display()
l1.insert_after(99,1)
l1.display()
l1.insert_before(98,3)
l1.display()
l1.delete_first()
l1.display()
l1.delete_last()
l1.display()