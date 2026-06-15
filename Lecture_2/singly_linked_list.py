#Here we are gonna implement a singly linked list
class node(object):
    def __init__(self, val):
        self.value = val
        self.next = None

class singly_linked_list(object):
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = node(val)

        if self.head is None:
            self.head = new_node
        
        
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node

    def insert_first(self, val):
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        self.head = self.head.next

    def delete(self, val):
        current = self.head

        if current is None:
            return

        if current.value == val:
            self.delete_first()

        else:
            while current.next.value != val:
                current = current.next

            current.next = current.next.next

    def search(self, val):
        current = self.head

        while current:
            if current.value == val:
                return True
            
            else:
                current = current.next

        return False
    
    def display(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print(None)   

        

l1 = singly_linked_list()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)

l1.display()
l1.insert_first(99)
l1.display()
l1.delete_first()
l1.display()
print(l1.search(4))
l1.delete(4)
l1.display()
print(l1.search(4))