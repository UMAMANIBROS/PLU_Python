#2.Insert a new node containing 25 after the node containing 20.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref:
                temp = temp.ref
            temp.ref = new_node
    def insert_after(self, key, data):
        temp = self.head
        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.ref = temp.ref
                temp.ref = new_node
                break
            temp = temp.ref
        print("Node not found")
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.ref
        print("None")
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print("Before Insertion:")
ll.display()
ll.insert_after(20, 25)
print("After Insertion:")
ll.display()