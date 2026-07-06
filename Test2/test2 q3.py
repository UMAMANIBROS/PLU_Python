#3.Delete the node containing 30 from the linked list and display the updated list.
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
    def delete(self, key):
        temp = self.head
        prev = None
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.ref
        if temp is None:
            print("Node not found")
        elif temp == self.head:
            self.head = self.head.ref
        else:
            prev.ref = temp.ref
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
print("Before Deletion:")
ll.display()
ll.delete(30)
print("After Deletion:")
ll.display()