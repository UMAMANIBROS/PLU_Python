# Question 1
#1.Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements.
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
print("Linked List:")
ll.display()