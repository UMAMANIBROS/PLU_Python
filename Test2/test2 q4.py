#4.Count and display the total number of nodes in the linked list
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
    def count_nodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.ref
        return count
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
print("Total Number of Nodes:", ll.count_nodes())
